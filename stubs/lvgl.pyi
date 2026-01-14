# SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
# Type stubs for lvgl (LVGL v9.3) based on uiflow-micropython repository

from typing import Callable, Optional, Any, List, Tuple

# Event constants
class EVENT:
    """LVGL event type constants."""
    ALL: int
    PRESSED: int
    PRESSING: int
    PRESS_LOST: int
    SHORT_CLICKED: int
    LONG_PRESSED: int
    LONG_PRESSED_REPEAT: int
    CLICKED: int
    RELEASED: int
    SCROLL_BEGIN: int
    SCROLL_THROW_BEGIN: int
    SCROLL_END: int
    SCROLL: int
    GESTURE: int
    KEY: int
    FOCUSED: int
    DEFOCUSED: int
    LEAVE: int
    HIT_TEST: int
    COVER_CHECK: int
    REFR_EXT_DRAW_SIZE: int
    DRAW_MAIN_BEGIN: int
    DRAW_MAIN: int
    DRAW_MAIN_END: int
    DRAW_POST_BEGIN: int
    DRAW_POST: int
    DRAW_POST_END: int
    DRAW_TASK_ADDED: int
    VALUE_CHANGED: int
    INSERT: int
    REFRESH: int
    READY: int
    CANCEL: int
    DELETE: int
    CHILD_CHANGED: int
    CHILD_CREATED: int
    CHILD_DELETED: int
    SCREEN_UNLOAD_START: int
    SCREEN_LOAD_START: int
    SCREEN_LOADED: int
    SCREEN_UNLOADED: int
    SIZE_CHANGED: int
    STYLE_CHANGED: int
    LAYOUT_CHANGED: int
    GET_SELF_SIZE: int

# State constants
class STATE:
    """LVGL state constants."""
    DEFAULT: int
    CHECKED: int
    FOCUSED: int
    FOCUS_KEY: int
    EDITED: int
    HOVERED: int
    PRESSED: int
    SCROLLED: int
    DISABLED: int
    USER_1: int
    USER_2: int
    USER_3: int
    USER_4: int
    ANY: int

# Part constants
class PART:
    """LVGL part constants."""
    MAIN: int
    SCROLLBAR: int
    INDICATOR: int
    KNOB: int
    SELECTED: int
    ITEMS: int
    CURSOR: int
    CUSTOM_FIRST: int
    ANY: int

# Alignment constants
class ALIGN:
    """LVGL alignment constants."""
    DEFAULT: int
    TOP_LEFT: int
    TOP_MID: int
    TOP_RIGHT: int
    BOTTOM_LEFT: int
    BOTTOM_MID: int
    BOTTOM_RIGHT: int
    LEFT_MID: int
    RIGHT_MID: int
    CENTER: int
    OUT_TOP_LEFT: int
    OUT_TOP_MID: int
    OUT_TOP_RIGHT: int
    OUT_BOTTOM_LEFT: int
    OUT_BOTTOM_MID: int
    OUT_BOTTOM_RIGHT: int
    OUT_LEFT_TOP: int
    OUT_LEFT_MID: int
    OUT_LEFT_BOTTOM: int
    OUT_RIGHT_TOP: int
    OUT_RIGHT_MID: int
    OUT_RIGHT_BOTTOM: int

# Opacity constants
class OPA:
    """LVGL opacity constants."""
    TRANSP: int = 0
    COVER: int = 255

# Flex constants
class FLEX_FLOW:
    """LVGL flex flow constants."""
    ROW: int
    COLUMN: int
    ROW_WRAP: int
    COLUMN_WRAP: int
    ROW_REVERSE: int
    COLUMN_REVERSE: int
    ROW_WRAP_REVERSE: int
    COLUMN_WRAP_REVERSE: int

# Border side constants
class BORDER_SIDE:
    """LVGL border side constants."""
    NONE: int
    BOTTOM: int
    TOP: int
    LEFT: int
    RIGHT: int
    FULL: int
    INTERNAL: int

# Symbol constants
class SYMBOL:
    """LVGL symbol/icon constants."""
    AUDIO: str
    VIDEO: str
    LIST: str
    OK: str
    CLOSE: str
    POWER: str
    SETTINGS: str
    HOME: str
    DOWNLOAD: str
    DRIVE: str
    REFRESH: str
    MUTE: str
    VOLUME_MID: str
    VOLUME_MAX: str
    IMAGE: str
    TINT: str
    PREV: str
    PLAY: str
    PAUSE: str
    STOP: str
    NEXT: str
    EJECT: str
    LEFT: str
    RIGHT: str
    PLUS: str
    MINUS: str
    EYE_OPEN: str
    EYE_CLOSE: str
    WARNING: str
    SHUFFLE: str
    UP: str
    DOWN: str
    LOOP: str
    DIRECTORY: str
    UPLOAD: str
    CALL: str
    CUT: str
    COPY: str
    SAVE: str
    BARS: str
    ENVELOPE: str
    CHARGE: str
    PASTE: str
    BELL: str
    KEYBOARD: str
    BACKSPACE: str
    SD_CARD: str
    NEW_LINE: str
    DUMMY: str
    BULLET: str
    BATTERY_FULL: str
    BATTERY_3: str
    BATTERY_2: str
    BATTERY_1: str
    BATTERY_EMPTY: str
    USB: str
    BLUETOOTH: str
    TRASH: str
    EDIT: str
    GPS: str
    FILE: str
    WIFI: str

# Style constants
class STYLE:
    """LVGL style property constants."""
    TRANSFORM_WIDTH: int
    TRANSFORM_HEIGHT: int
    TEXT_LETTER_SPACE: int

# Font objects
font_montserrat_8: Any
font_montserrat_10: Any
font_montserrat_12: Any
font_montserrat_14: Any
font_montserrat_16: Any
font_montserrat_18: Any
font_montserrat_20: Any
font_montserrat_22: Any
font_montserrat_24: Any
font_montserrat_26: Any
font_montserrat_28: Any
font_montserrat_30: Any
font_montserrat_32: Any
font_montserrat_34: Any
font_montserrat_36: Any
font_montserrat_38: Any
font_montserrat_40: Any
font_montserrat_42: Any
font_montserrat_44: Any
font_montserrat_46: Any
font_montserrat_48: Any

# Sizing constants
SIZE_CONTENT: int
DPI_DEF: int

def pct(value: int) -> int:
    """Convert percentage to LVGL percentage value."""
    ...

def color_hex(hex_value: int) -> Any:
    """Create a color from hexadecimal value."""
    ...

def screen_active() -> "obj":
    """Get the currently active screen."""
    ...

def screen_load(screen: "obj") -> None:
    """Load a screen as the active screen."""
    ...

def tick_inc(tick: int) -> None:
    """Increment the LVGL tick counter."""
    ...

def task_handler() -> None:
    """Run the LVGL task handler."""
    ...

class anim_t:
    """Animation object."""
    @staticmethod
    def path_overshoot(value: int) -> int: ...

class style_transition_dsc_t:
    """Style transition descriptor."""
    def init(
        self,
        props: List[int],
        path_cb: Callable,
        time: int,
        delay: int,
        user_data: Optional[Any]
    ) -> None: ...

class obj:
    """Base LVGL object class - parent of all widgets."""
    
    class FLAG:
        """Object flag constants."""
        HIDDEN: int
        CLICKABLE: int
        CLICK_FOCUSABLE: int
        CHECKABLE: int
        SCROLLABLE: int
        SCROLL_ELASTIC: int
        SCROLL_MOMENTUM: int
        SCROLL_ONE: int
        SCROLL_CHAIN_HOR: int
        SCROLL_CHAIN_VER: int
        SCROLL_CHAIN: int
        SCROLL_ON_FOCUS: int
        SCROLL_WITH_ARROW: int
        SNAPPABLE: int
        PRESS_LOCK: int
        EVENT_BUBBLE: int
        GESTURE_BUBBLE: int
        ADV_HITTEST: int
        IGNORE_LAYOUT: int
        FLOATING: int
        SEND_DRAW_TASK_EVENTS: int
        OVERFLOW_VISIBLE: int
        FLEX_IN_NEW_TRACK: int
        LAYOUT_1: int
        LAYOUT_2: int
        WIDGET_1: int
        WIDGET_2: int
        USER_1: int
        USER_2: int
        USER_3: int
        USER_4: int
    
    def __init__(self, parent: Optional["obj"] = None) -> None: ...
    
    def set_pos(self, x: int, y: int) -> None:
        """Set object position."""
        ...
    
    def set_x(self, x: int) -> None:
        """Set object X position."""
        ...
    
    def set_y(self, y: int) -> None:
        """Set object Y position."""
        ...
    
    def set_size(self, w: int, h: int) -> None:
        """Set object size."""
        ...
    
    def set_width(self, w: int) -> None:
        """Set object width."""
        ...
    
    def set_height(self, h: int) -> None:
        """Set object height."""
        ...
    
    def set_align(self, align: int) -> None:
        """Set object alignment."""
        ...
    
    def align_to(self, target: "obj", align: int, x_ofs: int, y_ofs: int) -> None:
        """Align this object relative to another object."""
        ...
    
    def add_flag(self, flag: int) -> None:
        """Add a flag to the object."""
        ...
    
    def remove_flag(self, flag: int) -> None:
        """Remove a flag from the object."""
        ...
    
    def has_flag(self, flag: int) -> bool:
        """Check if object has a specific flag."""
        ...
    
    def add_state(self, state: int) -> None:
        """Add a state to the object."""
        ...
    
    def clear_state(self, state: int) -> None:
        """Clear a state from the object."""
        ...
    
    def has_state(self, state: int) -> bool:
        """Check if object has a specific state."""
        ...
    
    def add_event_cb(self, cb: Callable, event_code: int, user_data: Optional[Any]) -> None:
        """Add an event callback to the object."""
        ...
    
    def set_style_bg_color(self, color: Any, selector: int) -> None:
        """Set background color style."""
        ...
    
    def set_style_bg_opa(self, opa: int, selector: int) -> None:
        """Set background opacity style."""
        ...
    
    def set_style_border_color(self, color: Any, selector: int) -> None:
        """Set border color style."""
        ...
    
    def set_style_border_opa(self, opa: int, selector: int) -> None:
        """Set border opacity style."""
        ...
    
    def set_style_border_width(self, width: int, selector: int) -> None:
        """Set border width style."""
        ...
    
    def set_style_border_side(self, side: int, selector: int) -> None:
        """Set border side style."""
        ...
    
    def set_style_text_color(self, color: Any, selector: int) -> None:
        """Set text color style."""
        ...
    
    def set_style_text_opa(self, opa: int, selector: int) -> None:
        """Set text opacity style."""
        ...
    
    def set_style_text_font(self, font: Any, selector: int) -> None:
        """Set text font style."""
        ...
    
    def set_style_pad_left(self, pad: int, selector: int) -> None:
        """Set left padding style."""
        ...
    
    def set_style_pad_right(self, pad: int, selector: int) -> None:
        """Set right padding style."""
        ...
    
    def set_style_pad_top(self, pad: int, selector: int) -> None:
        """Set top padding style."""
        ...
    
    def set_style_pad_bottom(self, pad: int, selector: int) -> None:
        """Set bottom padding style."""
        ...
    
    def set_style_margin_left(self, margin: int, selector: int) -> None:
        """Set left margin style."""
        ...
    
    def set_style_margin_right(self, margin: int, selector: int) -> None:
        """Set right margin style."""
        ...
    
    def set_style_margin_top(self, margin: int, selector: int) -> None:
        """Set top margin style."""
        ...
    
    def set_style_margin_bottom(self, margin: int, selector: int) -> None:
        """Set bottom margin style."""
        ...
    
    def set_style_radius(self, radius: int, selector: int) -> None:
        """Set corner radius style."""
        ...
    
    def set_style_line_color(self, color: Any, selector: int) -> None:
        """Set line color style."""
        ...
    
    def set_style_line_opa(self, opa: int, selector: int) -> None:
        """Set line opacity style."""
        ...
    
    def set_style_transform_width(self, width: int, selector: int) -> None:
        """Set transform width style."""
        ...
    
    def set_style_transform_height(self, height: int, selector: int) -> None:
        """Set transform height style."""
        ...
    
    def set_style_transition(self, trans: style_transition_dsc_t, selector: int) -> None:
        """Set transition style."""
        ...
    
    def get_style_transition(self, selector: int) -> style_transition_dsc_t:
        """Get transition style."""
        ...
    
    def set_flex_flow(self, flow: int) -> None:
        """Set flex flow layout."""
        ...
    
    def get_parent(self) -> Optional["obj"]:
        """Get parent object."""
        ...
    
    def get_width(self) -> int:
        """Get object width."""
        ...
    
    def get_height(self) -> int:
        """Get object height."""
        ...
    
    def get_style_pad_left(self, part: int) -> int:
        """Get left padding."""
        ...
    
    def get_style_pad_right(self, part: int) -> int:
        """Get right padding."""
        ...
    
    def get_style_pad_top(self, part: int) -> int:
        """Get top padding."""
        ...
    
    def get_style_pad_bottom(self, part: int) -> int:
        """Get bottom padding."""
        ...
    
    def get_style_text_font(self, part: int) -> Any:
        """Get text font."""
        ...
    
    def move_to_index(self, index: int) -> None:
        """Move object to specific index in parent's children."""
        ...
    
    def delete(self) -> None:
        """Delete the object."""
        ...

class label(obj):
    """Label widget for displaying text."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...
    def set_text(self, text: str) -> None: ...
    def get_text(self) -> str: ...

class button(obj):
    """Button widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class list(obj):
    """List container widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class msgbox(obj):
    """Message box dialog widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...
    def add_title(self, title: str) -> None: ...
    def get_header(self) -> Optional[obj]: ...
    def get_footer(self) -> Optional[obj]: ...
    def get_content(self) -> Optional[obj]: ...
    def add_footer_button(self, text: str) -> button: ...

class textarea(obj):
    """Text area input widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...
    def set_text(self, text: str) -> None: ...
    def set_placeholder_text(self, text: str) -> None: ...
    def set_one_line(self, en: bool) -> None: ...

class buttonmatrix(obj):
    """Button matrix widget."""
    class CTRL:
        """Button matrix control flags."""
        HIDDEN: int
        NO_REPEAT: int
        DISABLED: int
        CHECKABLE: int
        CHECKED: int
        CLICK_TRIG: int
        POPOVER: int
        CUSTOM_1: int
        CUSTOM_2: int
    
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class switch(obj):
    """Switch/toggle widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class checkbox(obj):
    """Checkbox widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class slider(obj):
    """Slider widget."""
    class MODE:
        """Slider mode constants."""
        NORMAL: int
        SYMMETRICAL: int
        RANGE: int
    
    def __init__(self, parent: Optional[obj] = None) -> None: ...
    def set_value(self, value: int, anim: bool) -> None: ...
    def set_range(self, min_val: int, max_val: int) -> None: ...
    def get_value(self) -> int: ...
    def get_min_value(self) -> int: ...
    def get_max_value(self) -> int: ...
    def set_mode(self, mode: int) -> None: ...

class arc(obj):
    """Arc/circular progress widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class bar(obj):
    """Progress bar widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class keyboard(obj):
    """Keyboard widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class image(obj):
    """Image widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...
    def set_src(self, src: Any) -> None: ...

class led(obj):
    """LED indicator widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class win(obj):
    """Window container widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class menu(obj):
    """Menu widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class chart(obj):
    """Chart/graph widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class dropdown(obj):
    """Dropdown selection widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class roller(obj):
    """Roller selection widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class spinbox(obj):
    """Spinbox number input widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class table(obj):
    """Table data display widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class tabview(obj):
    """Tab view container widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class canvas(obj):
    """Canvas for custom drawing."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class calendar(obj):
    """Calendar date picker widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class spinner(obj):
    """Loading spinner widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class line(obj):
    """Line drawing widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...

class scale(obj):
    """Scale/gauge widget."""
    def __init__(self, parent: Optional[obj] = None) -> None: ...
