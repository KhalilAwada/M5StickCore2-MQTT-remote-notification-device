# M5Stack Core 2 Development Environment

This project is configured with a DevContainer for M5Stack Core 2 development with UIFlow2 firmware.

## Prerequisites

- Docker installed on your system
- VS Code with Dev Containers extension
- M5Stack Core 2 with UIFlow2 firmware flashed

## Getting Started

1. **Open in DevContainer**
   - Open this folder in VS Code
   - Click "Reopen in Container" when prompted
   - Or use Command Palette: `Dev Containers: Reopen in Container`

2. **Connect Your M5Stack**
   - Connect your M5Stack Core 2 via USB
   - The device should be accessible in the container at `/dev/ttyACM0` or `/dev/ttyUSB0`

3. **Upload Code**
   ```bash
   ./upload.sh main.py
   ```

## Project Structure

```
.
├── .devcontainer/
│   ├── devcontainer.json    # DevContainer configuration
│   ├── Dockerfile            # Container image definition
│   └── requirements.txt      # Python dependencies
├── main.py                   # Your main M5Stack code
├── upload.sh                 # Upload script for M5Stack
└── README.md                 # This file
```

## Available Tools

The DevContainer includes:

- **Python 3.11** - Latest stable Python version
- **esptool** - ESP32 flashing tool
- **ampy** - Adafruit MicroPython tool for file management
- **mpremote** - MicroPython remote control
- **rshell** - Remote shell for MicroPython
- **pyserial** - Serial communication library

## Usage

### Upload Code to M5Stack

```bash
# Upload main.py (default)
./upload.sh

# Upload a specific file
./upload.sh your_file.py

# Set custom port
M5STACK_PORT=/dev/ttyUSB0 ./upload.sh main.py
```

### Find Connected Device

```bash
# List all USB serial devices
ls -l /dev/tty*

# Or use lsusb
lsusb
```

### Interactive MicroPython REPL

```bash
# Using mpremote
mpremote connect /dev/ttyACM0

# Using screen
screen /dev/ttyACM0 115200

# Using picocom
picocom /dev/ttyACM0 -b 115200
```

### File Management

```bash
# List files on M5Stack
ampy --port /dev/ttyACM0 ls

# Get a file from M5Stack
ampy --port /dev/ttyACM0 get boot.py

# Remove a file
ampy --port /dev/ttyACM0 rm old_file.py
```

## Example Code

The included `main.py` demonstrates:
- Display initialization
- Touch screen input
- Text rendering
- Basic event loop

## Troubleshooting

### Device not found

1. Check USB connection
2. Verify the device appears on your host:
   - macOS: `ls /dev/cu.*` or `ls /dev/tty.*`
   - Linux: `ls /dev/ttyUSB* /dev/ttyACM*`
3. Ensure the container has USB access (configured in devcontainer.json)

### Upload fails

1. Try a different USB cable (must support data transfer)
2. Press and hold the reset button while uploading
3. Check baud rate (default: 115200)
4. Verify UIFlow2 firmware is installed

### Permission denied

```bash
# On Linux host, add your user to dialout group
sudo usermod -a -G dialout $USER
# Then log out and back in
```

## M5Stack Core 2 Resources

- [M5Stack Documentation](https://docs.m5stack.com/)
- [UIFlow2 Documentation](https://docs.m5stack.com/en/uiflow/uiflow_home_page)
- [M5Stack GitHub](https://github.com/m5stack)
- [MicroPython Documentation](https://docs.micropython.org/)

## Development Tips

1. **Auto-reload**: UIFlow2 supports auto-reload on file save
2. **Debugging**: Use `print()` statements and view output via serial monitor
3. **Libraries**: Place custom libraries in `/flash/lib/` on the device
4. **Error Handling**: Always use try-except blocks for robust code

## License

MIT License - Feel free to use this template for your projects!
