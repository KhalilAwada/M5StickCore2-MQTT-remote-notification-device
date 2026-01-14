# SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
# Type stubs for m5ui module based on uiflow-micropython repository

from typing import Callable, Optional, Any
import lvgl as lv

def init() -> None:
    """Initialize M5UI library and event loop."""
    ...

def deinit() -> None:
    """Deinitialize M5UI library."""
    ...

def event_loop(freq: int = 33, max_scheduled: int = 2) -> Any:
    """Create or get the M5UI event loop instance."""
    ...

class M5Page(lv.obj):
    """Page container widget - represents a full screen.
    
    Args:
        bg_c: Background color in hexadecimal format (default: 0xFFFFFF)
    """
    def __init__(self, bg_c: int = 0xFFFFFF) -> None: ...
    
    def screen_load(self) -> None:
        """Load this page as the active screen."""
        ...
    
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...
    def set_state(self, state: int, value: bool) -> None: ...
    def toggle_state(self, state: int) -> None: ...
    def set_text_color(self, color: int, opa: int, part: int) -> None: ...
    def set_bg_color(self, color: int, opa: int, part: int) -> None: ...

class M5Label(lv.label):
    """Text label widget.
    
    Args:
        text: The text to display
        x: X position (default: 0)
        y: Y position (default: 0)
        text_c: Text color in hex (default: 0x212121)
        bg_c: Background color in hex (default: 0xFFFFFF)
        bg_opa: Background opacity 0-255 (default: 0)
        font: LVGL font object (default: lv.font_montserrat_14)
        parent: Parent object (default: active screen)
    """
    def __init__(
        self,
        text: str,
        x: int = 0,
        y: int = 0,
        text_c: int = 0x212121,
        bg_c: int = 0xFFFFFF,
        bg_opa: int = 0,
        font: Any = ...,
        parent: Optional[lv.obj] = None
    ) -> None: ...
    
    def set_shadow(self, color: int, opa: int, align: int, offset_x: int, offset_y: int) -> None:
        """Set a shadow for the label."""
        ...
    
    def unset_shadow(self) -> None:
        """Remove the shadow from the label."""
        ...
    
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...
    def set_text_color(self, color: int, opa: int, part: int) -> None: ...
    def set_bg_color(self, color: int, opa: int, part: int) -> None: ...

class M5Button(lv.button):
    """Button widget.
    
    Args:
        text: Button text (default: "button0")
        x: X position (default: 0)
        y: Y position (default: 0)
        w: Width, 0 for auto (default: 0)
        h: Height, 0 for auto (default: 0)
        bg_c: Background color in hex (default: 0x2196F3)
        text_c: Text color in hex (default: 0xFFFFFF)
        font: LVGL font object (default: lv.font_montserrat_14)
        parent: Parent object (default: active screen)
    """
    
    EFFECT_SIMPLE: int = 0
    EFFECT_WAVE: int = 1
    EFFECT_GUMMY: int = 2
    
    def __init__(
        self,
        text: str = "button0",
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        bg_c: int = 0x2196F3,
        text_c: int = 0xFFFFFF,
        font: Any = ...,
        parent: Optional[lv.obj] = None
    ) -> None: ...
    
    def set_btn_text(self, text: str) -> None:
        """Set the button text."""
        ...
    
    def get_btn_text(self) -> str:
        """Get the button text."""
        ...
    
    def set_pressed_effect(self, effect: int) -> None:
        """Set the button press effect (EFFECT_SIMPLE, EFFECT_WAVE, EFFECT_GUMMY)."""
        ...
    
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...
    def set_text_color(self, color: int, opa: int, part: int) -> None: ...
    def set_bg_color(self, color: int, opa: int, part: int) -> None: ...

class M5List(lv.list):
    """List widget container.
    
    Args:
        x: X position (default: 0)
        y: Y position (default: 0)
        w: Width (default: 0)
        h: Height (default: 0)
        parent: Parent object (default: active screen)
    """
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        parent: Optional[lv.obj] = None
    ) -> None: ...
    
    def add_text(
        self,
        text: str,
        text_c: int = 0x212121,
        text_opa: int = 255,
        bg_c: int = 0xE6E2E6,
        bg_opa: int = 255,
        font: Any = ...
    ) -> M5Label:
        """Add a text label to the list."""
        ...
    
    def add_button(
        self,
        icon: Optional[str],
        text: str = "button0",
        h: int = 0,
        bg_c: int = 0xFFFFFF,
        bg_opa: int = 255,
        text_c: int = 0x000000,
        text_opa: int = 255,
        font: Any = ...
    ) -> M5Button:
        """Add a button to the list."""
        ...
    
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Msgbox(lv.msgbox):
    """Message box dialog widget.
    
    Args:
        title: Title text (default: "")
        x: X position (default: 0)
        y: Y position (default: 0)
        w: Width (default: 0)
        h: Height (default: 0)
        parent: Parent object (default: active screen)
    """
    def __init__(
        self,
        title: str = "",
        x: int = 0,
        y: int = 0,
        w: int = 0,
        h: int = 0,
        parent: Optional[lv.obj] = None
    ) -> None: ...
    
    def add_text(
        self,
        text: str,
        text_c: int = 0x212121,
        text_opa: int = 255,
        bg_c: int = 0xFFFFFF,
        bg_opa: int = 255,
        font: Any = ...
    ) -> M5Label:
        """Add text content to the message box."""
        ...
    
    def add_button(
        self,
        icon: Optional[str] = None,
        text: str = "",
        bg_c: int = 0x2196F3,
        bg_opa: int = 255,
        text_c: int = 0xFFFFFF,
        text_opa: int = 255,
        font: Any = ...,
        option: str = "footer"
    ) -> M5Button:
        """Add a button to the message box (option: 'header' or 'footer')."""
        ...
    
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5TextArea(lv.textarea):
    """Text area input widget.
    
    Args:
        text: Initial text content (default: "")
        placeholder: Placeholder text (default: "")
        x: X position (default: 0)
        y: Y position (default: 0)
        w: Width (default: 200)
        h: Height (default: 100)
        font: LVGL font object (default: lv.font_montserrat_14)
        bg_c: Background color (default: 0xFFFFFF)
        border_c: Border color (default: 0xE0E0E0)
        text_c: Text color (default: 0x212121)
        parent: Parent object (default: active screen)
    """
    def __init__(
        self,
        text: str = "",
        placeholder: str = "",
        x: int = 0,
        y: int = 0,
        w: int = 200,
        h: int = 100,
        font: Any = ...,
        bg_c: int = 0xFFFFFF,
        border_c: int = 0xE0E0E0,
        text_c: int = 0x212121,
        parent: Optional[lv.obj] = None
    ) -> None: ...
    
    def set_one_line(self, en: bool) -> None:
        """Set single line or multi-line mode."""
        ...
    
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...
    def set_text_color(self, color: int, opa: int, part: int) -> None: ...
    def set_bg_color(self, color: int, opa: int, part: int) -> None: ...

class M5ButtonMatrix(lv.buttonmatrix):
    """Button matrix widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Switch(lv.switch):
    """Switch/toggle widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Checkbox(lv.checkbox):
    """Checkbox widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Slider(lv.slider):
    """Slider widget.
    
    Args:
        x: X position (default: 0)
        y: Y position (default: 0)
        w: Width (default: 100)
        h: Height (default: 20)
        mode: Slider mode (default: lv.slider.MODE.NORMAL)
        min_value: Minimum value (default: 0)
        max_value: Maximum value (default: 100)
        value: Initial value (default: 25)
        bg_c: Background color (default: 0x2193F3)
        color: Indicator color (default: 0x2193F3)
        parent: Parent object (default: active screen)
    """
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        w: int = 100,
        h: int = 20,
        mode: int = ...,
        min_value: int = 0,
        max_value: int = 100,
        value: int = 25,
        bg_c: int = 0x2193F3,
        color: int = 0x2193F3,
        parent: Optional[lv.obj] = None
    ) -> None: ...
    
    def set_value(self, value: int, anim: bool = False) -> None:
        """Set the slider value."""
        ...
    
    def set_range(self, min_value: int, max_value: int) -> None:
        """Set the slider range."""
        ...
    
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Arc(lv.arc):
    """Arc/circular progress widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Bar(lv.bar):
    """Progress bar widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Keyboard(lv.keyboard):
    """Keyboard widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5LED(lv.led):
    """LED indicator widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Win(lv.win):
    """Window container widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Menu(lv.menu):
    """Menu widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Image(lv.image):
    """Image display widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Chart(lv.chart):
    """Chart/graph widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Dropdown(lv.dropdown):
    """Dropdown selection widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Roller(lv.roller):
    """Roller selection widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Spinbox(lv.spinbox):
    """Spinbox number input widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Table(lv.table):
    """Table data display widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5TabView(lv.tabview):
    """Tab view container widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Canvas(lv.canvas):
    """Canvas for custom drawing."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Calendar(lv.calendar):
    """Calendar date picker widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Spinner(lv.spinner):
    """Loading spinner widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Line(lv.line):
    """Line drawing widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...

class M5Scale(lv.scale):
    """Scale/gauge widget."""
    def __init__(self, parent: Optional[lv.obj] = None) -> None: ...
    def set_flag(self, flag: int, value: bool) -> None: ...
    def toggle_flag(self, flag: int) -> None: ...
