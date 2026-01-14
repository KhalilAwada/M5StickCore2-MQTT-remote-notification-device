# MicroPython Type Stubs

This directory contains Python stub files (`.pyi`) for M5Stack MicroPython libraries. These stubs provide type hints and IDE support for libraries that only exist on the M5Stack device.

## Structure

```
stubs/
├── M5/
│   └── __init__.pyi      # M5 module stubs (BtnA, Widgets, Touch)
├── hardware/
│   ├── __init__.pyi
│   └── sdcard.pyi        # SD card hardware module
├── m5ui.pyi              # M5UI widgets (M5Page, M5Label, M5List, etc.)
└── lvgl.pyi              # LVGL bindings
```

## Usage

These stubs are automatically recognized by VSCode through the settings in `.vscode/settings.json`. They provide:
- Auto-completion for M5Stack functions and classes
- Type checking
- IntelliSense support
- Eliminates "module not found" errors

## Updating Stubs

If you need to add more M5Stack APIs:
1. Add the function/class signature to the appropriate `.pyi` file
2. Use Python type hints (from `typing` module)
3. Add docstrings for better IDE support

## Reference

Official M5Stack UIFlow MicroPython repository:
https://github.com/m5stack/uiflow-micropython
