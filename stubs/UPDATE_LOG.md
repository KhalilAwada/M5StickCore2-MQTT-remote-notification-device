# Type Stubs Update - January 14, 2026

## Summary

Successfully updated all M5Stack MicroPython type stubs based on the official **uiflow-micropython** repository source code.

## Updated Files

### 1. `/stubs/M5/__init__.pyi`
**Source:** `m5stack/components/M5Unified/mpy_m5*.cpp`

**Complete API Coverage:**
- **Button class**: Full hardware button interface with all methods
  - State checking: `isHolding()`, `isPressed()`, `wasClicked()`, `wasDoubleClicked()`, etc.
  - Configuration: `setDebounceThresh()`, `setHoldThresh()`
  - Callbacks: `setCallback()`, `removeCallback()` with CB_TYPE constants
  - All 5 button instances: `BtnA`, `BtnB`, `BtnC`, `BtnPWR`, `BtnEXT`

- **Touch class**: Touch screen interface
  - Position: `getX()`, `getY()`, `getCount()`
  - Details: `getDetail()` returns 11-element tuple with touch state
  - Raw data: `getTouchPointRaw()` returns (x, y, size, id)

- **Widgets class**: Legacy M5GFX-style widgets
  - Label, Rectangle, Circle, Triangle, QRCode
  - Font constants (DejaVu9 through DejaVu72)

- **Board enumeration**: Board type constants
- **Display interface**: Basic display methods
- **Module functions**: `begin()`, `update()`, `getBoard()`

### 2. `/stubs/m5ui.pyi`
**Source:** `m5stack/libs/m5ui/*.py`

**Complete Widget Library (25+ classes):**
- **Core widgets**: M5Page, M5Label, M5Button, M5List, M5Msgbox
- **Input widgets**: M5TextArea, M5Keyboard, M5Slider, M5Checkbox, M5Switch, M5Spinbox
- **Display widgets**: M5Image, M5Chart, M5Canvas, M5LED, M5Spinner, M5Scale
- **Container widgets**: M5Win, M5Menu, M5TabView, M5Calendar
- **Advanced widgets**: M5ButtonMatrix, M5Dropdown, M5Roller, M5Table, M5Arc, M5Bar, M5Line

**All widgets include:**
- Complete constructor signatures with all parameters and defaults
- Specific methods (e.g., `set_btn_text()` for M5Button, `add_text()` for M5List)
- Common base methods from M5Base: `set_flag()`, `toggle_flag()`, `set_state()`, `set_text_color()`, `set_bg_color()`
- Proper inheritance from corresponding LVGL base classes

**Module functions:**
- `init()`: Initialize M5UI library
- `deinit()`: Cleanup M5UI
- `event_loop()`: Event loop management

### 3. `/stubs/lvgl.pyi`
**Source:** LVGL v9.3 bindings in M5Stack firmware + `m5stack/libs/m5ui/*.py` usage patterns

**Complete LVGL API:**
- **Event constants** (EVENT): 40+ event types including PRESSED, CLICKED, VALUE_CHANGED, FOCUSED, etc.
- **State constants** (STATE): DEFAULT, CHECKED, FOCUSED, PRESSED, DISABLED, etc.
- **Part constants** (PART): MAIN, INDICATOR, KNOB, SCROLLBAR, etc.
- **Alignment** (ALIGN): 24+ alignment options (CENTER, TOP_LEFT, BOTTOM_RIGHT, OUT_*, etc.)
- **Opacity** (OPA): TRANSP (0), COVER (255)
- **Flex layout** (FLEX_FLOW): ROW, COLUMN, WRAP variants, REVERSE variants
- **Border sides** (BORDER_SIDE): NONE, BOTTOM, TOP, LEFT, RIGHT, FULL, INTERNAL
- **Symbols** (SYMBOL): 50+ icon constants (HOME, SETTINGS, BULLET, WIFI, etc.)
- **Style properties** (STYLE): Transform and text properties

**Fonts:**
- Complete Montserrat font family: `font_montserrat_8` through `font_montserrat_48` (21 sizes)

**Base obj class:**
- 40+ methods covering positioning, sizing, alignment, styling, events, states, flags
- Complete style setters: colors, opacity, padding, margin, borders, transforms
- Event handling: `add_event_cb()`
- Layout: flex flow support

**All widget classes:**
- label, button, list, msgbox, textarea, buttonmatrix, switch, checkbox
- slider (with MODE constants), arc, bar, keyboard, image, led
- win, menu, chart, dropdown, roller, spinbox, table, tabview
- canvas, calendar, spinner, line, scale

**Module functions:**
- Color handling: `color_hex()`, `pct()`
- Screen management: `screen_active()`, `screen_load()`
- Event loop: `tick_inc()`, `task_handler()`

## Verification

✅ **No VSCode errors in main.py**
- All imports properly recognized
- Type hints working correctly
- IntelliSense fully functional

## Source Repository

All stubs based on: **github.com/m5stack/uiflow-micropython**
- Cloned: January 14, 2026
- Commit: Latest from main branch (depth=1 clone)
- License: MIT (SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD)

## Key Improvements from Previous Stubs

1. **Accuracy**: Based on actual source code, not hand-crafted assumptions
2. **Completeness**: All 25+ m5ui widgets with full signatures
3. **Documentation**: Proper docstrings from official source
4. **Type safety**: Complete type hints for better IDE support
5. **LVGL v9.3**: Full event system, state management, and style properties
6. **Button API**: Complete hardware button interface with callbacks
7. **Touch API**: Full touch screen interface with detailed state
