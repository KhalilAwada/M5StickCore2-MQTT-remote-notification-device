# MQTT Messages Reference

This document describes the MQTT messages currently handled by the M5Stack Core 2 firmware in [main.py](main.py).

## Connection

MQTT credentials are loaded from `/sd/mqtt.json` (see [sample-sd-files/mqtt.json](sample-sd-files/mqtt.json)).

| Field | Description | Example |
|-------|-------------|---------|
| `client` | MQTT client identifier | `M5StackCore2Client` |
| `server` | Broker hostname | `mqtt.stardust.applink.ninja` |
| `port` | Broker port (TLS) | `8883` |
| `username` | Broker username | `applink` |
| `password` | Broker password | `***` |
| `topic` (optional) | Subscribed topic; defaults to `m5stack-notifications/github/all` | `m5stack-notifications/github/all` |

The client connects with TLS (`ssl=True`), `keepalive=60`, and a persistent session (`clean_session=False`). See [`connectMQTT()`](main.py#L480).

## Message Routing

Incoming messages enter at [`mqtt_callback()`](main.py#L356) and are dispatched by [`handleMQTTMessage()`](main.py#L364):

1. The payload is parsed as JSON.
2. If the payload is a dict with `messageType == "event"` and `messageGroup` in `("github", "grafana")`, it is routed to [`handleEventMessage()`](main.py#L403) where it is cached, deduplicated by `id`, persisted to SD, and rendered in the shared messages list.
3. Any other JSON dict is rendered generically on the dashboard MQTT status label.
4. Non-JSON payloads are displayed verbatim (truncated to 80 chars).

## Supported Message Types

### 1. GitHub Event Message

Routed to `handleEventMessage()` and cached/persisted to `/sd/mqtt-messages.json`. Only the latest 5 messages are retained (shared across github & grafana). Messages with the same `id` are deduplicated (replaced).

#### Required Discriminator Fields

| Field | Type | Required | Value |
|-------|------|----------|-------|
| `messageType` | string | yes | `"event"` |
| `messageGroup` | string | yes | `"github"` |
| `id` | string/number | yes | Unique message identifier (used for dedup) |

Messages without an `id` are dropped with a warning.

#### Display / Content Fields

| Field | Type | Used For |
|-------|------|----------|
| `lines` | array of strings | Primary text shown in the GitHub list (joined by `\n`, truncated to 200 chars). |
| `repository` | string | Fallback display when `lines` is missing: `"<repository> - <type>"`. |
| `type` | string | Fallback display label alongside `repository`. |
| `color` | string (hex like `"0xRRGGBB"`) or int | List item text color. Default `0x000000`. |
| `bgColor` | string (hex like `"0xRRGGBB"`) or int | List item background color. Default `0xffffff`. |

See [`updateGitHubList()`](main.py#L310).

#### Notification Sound Fields

[`playNotificationSound()`](main.py#L529) selects a tone pattern based on:

| `messageGroup` | `status` | `conclusion` | Sound |
|----------------|----------|--------------|-------|
| `github` | `"completed"` | `"success"` | Cheerful ascending melody (C-E-G-C-C-G) |
| `github` | `"completed"` | anything else | Sad descending tones (E-C-A-G-E) |
| `github` | anything else | — | Generic notification (G-C-G-C) |

#### Side Effects on Receipt

- Screen wakes up ([`wakeScreen()`](main.py)).
- Notification sound plays at user-configured volume.
- Message inserted at index 0 of the in-memory cache and persisted to `/sd/mqtt-messages.json`.
- GitHub page list re-rendered.

#### Example Payload

```json
{
  "messageType": "event",
  "messageGroup": "github",
  "id": "ci-run-12345",
  "repository": "owner/repo",
  "type": "workflow_run",
  "status": "completed",
  "conclusion": "success",
  "lines": [
    "owner/repo",
    "CI build #42",
    "✓ success"
  ],
  "color": "0x000000",
  "bgColor": "0xccffcc"
}
```

### 2. Grafana Alert Message

Routed to the same `handleEventMessage()` as GitHub events and stored in the same cache (`/sd/mqtt-messages.json`, max 5, dedup by `id`). Rendered in the same messages list on the GitHub page.

#### Required Discriminator Fields

| Field | Type | Required | Value |
|-------|------|----------|-------|
| `messageType` | string | yes | `"event"` |
| `messageGroup` | string | yes | `"grafana"` |
| `id` | string/number | yes | Unique alert identifier (used for dedup; `firing` → `resolved` for the same `id` replaces the entry) |
| `status` | string | yes | `"firing"` or `"resolved"` |

#### Display / Content Fields

| Field | Type | Used For |
|-------|------|----------|
| `lines` | array of strings | Primary text shown in the list (joined by `\n`, truncated to 200 chars). |
| `color` | string (hex `"0xRRGGBB"`) or int | Text color. If omitted, falls back to `0x000000`. |
| `bgColor` | string (hex `"0xRRGGBB"`) or int | Item background color. If omitted, defaults to red (`0xff6666`) for `firing` and green (`0x66cc66`) for `resolved`. Explicit values always win. |

#### Notification Sound

| `status` | Sound |
|----------|-------|
| `"firing"` | Urgent alarm (alternating 1200 / 800 Hz, 5 pulses) |
| `"resolved"` | Calm ascending C-E-G chord |

#### Side Effects on Receipt

Identical to GitHub events: wake screen, play sound, insert at index 0, persist, re-render list.

#### Example Payloads

```json
{
  "messageType": "event",
  "messageGroup": "grafana",
  "id": "alert-cpu-high-prod-01",
  "status": "firing",
  "color": "0x000000",
  "bgColor": "0xff9966",
  "lines": [
    "CPU > 90% on prod-01",
    "5m avg: 94%"
  ]
}
```

```json
{
  "messageType": "event",
  "messageGroup": "grafana",
  "id": "alert-cpu-high-prod-01",
  "status": "resolved",
  "lines": [
    "CPU back to normal on prod-01"
  ]
}
```

### 3. Generic JSON Object

Any JSON object that does not match the GitHub discriminator is rendered as key/value lines on `dashboard_page_label_mqtt_status`, prefixed with the topic. Truncated to 100 characters. Not cached, not persisted, no sound.

#### Example Payload

```json
{
  "temperature": 22.5,
  "humidity": 60
}
```

Displayed as:

```
Topic: <topic>
temperature: 22.5
humidity: 60
```

### 4. Non-JSON / Plain-Text Payload

If `json.loads()` raises `JSONDecodeError`, the raw payload is shown on the dashboard MQTT status label as `"<topic>:\n<message>"` (truncated to 80 chars). No further processing.

## Persistence

Cached event messages (github + grafana share the same store) are written to `/sd/mqtt-messages.json` by [`saveMQTTMessagesToSD()`](main.py#L459) and reloaded on boot by [`loadMQTTMessages()`](main.py#L350). Sample file: [sample-sd-files/mqtt-messages.json](sample-sd-files/mqtt-messages.json).

## Summary Table

| Type | Discriminator | Cached | Plays Sound | Wakes Screen | Render Target |
|------|---------------|--------|-------------|--------------|---------------|
| GitHub event | `messageType="event"` & `messageGroup="github"` | Yes (shared 5 max, dedup by `id`) | Yes | Yes | GitHub page list |
| Grafana alert | `messageType="event"` & `messageGroup="grafana"` | Yes (shared 5 max, dedup by `id`) | Yes (firing / resolved) | Yes | GitHub page list |
| Generic JSON dict | any other JSON object | No | No | No | Dashboard MQTT label |
| Plain text | non-JSON payload | No | No | No | Dashboard MQTT label |
