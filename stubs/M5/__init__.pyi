# SPDX-FileCopyrightText: 2025 M5Stack Technology CO LTD
# Type stubs for M5 module based on uiflow-micropython repository

from typing import Callable, Optional, Tuple

class Button:
    """M5Stack hardware button class.
    
    Provides methods to check button state and register callbacks.
    """
    
    # Callback type constants
    class CB_TYPE:
        WAS_CLICKED: int = 0
        WAS_DOUBLECLICKED: int = 1
        WAS_HOLD: int = 2
        WAS_PRESSED: int = 3
        WAS_RELEASED: int = 4
    
    def isHolding(self) -> bool:
        """Check if button is currently being held."""
        ...
    
    def isPressed(self) -> bool:
        """Check if button is currently pressed."""
        ...
    
    def isReleased(self) -> bool:
        """Check if button is currently released."""
        ...
    
    def wasChangePressed(self) -> bool:
        """Check if button press state changed."""
        ...
    
    def wasClicked(self) -> bool:
        """Check if button was clicked."""
        ...
    
    def wasHold(self) -> bool:
        """Check if button was held."""
        ...
    
    def wasPressed(self) -> bool:
        """Check if button was pressed."""
        ...
    
    def wasReleased(self) -> bool:
        """Check if button was released."""
        ...
    
    def wasSingleClicked(self) -> bool:
        """Check if button was single clicked."""
        ...
    
    def wasDoubleClicked(self) -> bool:
        """Check if button was double clicked."""
        ...
    
    def wasDeciedClickCount(self) -> bool:
        """Check if click count was decided."""
        ...
    
    def getClickCount(self) -> int:
        """Get the number of clicks."""
        ...
    
    def lastChange(self) -> int:
        """Get the time of the last state change."""
        ...
    
    def pressedFor(self, msec: int) -> bool:
        """Check if button has been pressed for at least msec milliseconds."""
        ...
    
    def releasedFor(self, msec: int) -> bool:
        """Check if button has been released for at least msec milliseconds."""
        ...
    
    def setDebounceThresh(self, msec: int) -> None:
        """Set the debounce threshold in milliseconds."""
        ...
    
    def setHoldThresh(self, msec: int) -> None:
        """Set the hold threshold in milliseconds."""
        ...
    
    def setCallback(self, type: int, cb: Callable[[], None]) -> None:
        """Register a callback for button events.
        
        Args:
            type: One of CB_TYPE constants
            cb: Callback function to be called when event occurs
        """
        ...
    
    def removeCallback(self, type: int) -> None:
        """Remove a registered callback.
        
        Args:
            type: One of CB_TYPE constants
        """
        ...

# Button instances
BtnA: Button
BtnB: Button
BtnC: Button
BtnPWR: Button
BtnEXT: Button

class Touch:
    """Touch screen interface for M5Stack devices."""
    
    def getX(self) -> int:
        """Get X coordinate of the first touch point."""
        ...
    
    def getY(self) -> int:
        """Get Y coordinate of the first touch point."""
        ...
    
    def getCount(self) -> int:
        """Get the number of touch points."""
        ...
    
    def getDetail(self, i: int = 0) -> Tuple[int, int, int, int, bool, bool, bool, bool, bool, bool, bool]:
        """Get detailed touch information for touch point i.
        
        Returns tuple of:
            (deltaX, deltaY, distanceX, distanceY, isPressed, wasPressed, 
             wasClicked, isReleased, wasReleased, isHolding, wasHold)
        """
        ...
    
    def getTouchPointRaw(self, i: int = 0) -> Tuple[int, int, int, int]:
        """Get raw touch point data for touch point i.
        
        Returns tuple of: (x, y, size, id)
        """
        ...

class Widgets:
    """Legacy M5GFX-style widgets for display rendering."""
    
    class Label:
        """Text label widget."""
        def __init__(
            self,
            text: str,
            x: int,
            y: int,
            text_c: int = 0xFFFFFF,
            bg_c: int = 0x000000,
            font: Optional[object] = None,
            parent: Optional[object] = None
        ) -> None: ...
        
        def setText(self, text: str) -> None:
            """Update the label text."""
            ...
        
        def setColor(self, text_c: int, bg_c: int = -1) -> None:
            """Set text and background colors."""
            ...
    
    class Rectangle:
        """Rectangle widget."""
        def __init__(
            self,
            x: int,
            y: int,
            w: int,
            h: int,
            bg_c: int = 0xFFFFFF,
            fg_c: int = 0x000000,
            parent: Optional[object] = None
        ) -> None: ...
    
    class Circle:
        """Circle widget."""
        def __init__(
            self,
            x: int,
            y: int,
            r: int,
            bg_c: int = 0xFFFFFF,
            fg_c: int = 0x000000,
            parent: Optional[object] = None
        ) -> None: ...
    
    class Triangle:
        """Triangle widget."""
        def __init__(
            self,
            x0: int,
            y0: int,
            x1: int,
            y1: int,
            x2: int,
            y2: int,
            bg_c: int = 0xFFFFFF,
            fg_c: int = 0x000000,
            parent: Optional[object] = None
        ) -> None: ...
    
    class QRCode:
        """QR Code widget."""
        def __init__(
            self,
            text: str,
            x: int,
            y: int,
            w: int = 100,
            fg_c: int = 0x000000,
            bg_c: int = 0xFFFFFF,
            parent: Optional[object] = None
        ) -> None: ...
    
    # Font constants
    class FONTS:
        DejaVu9: object
        DejaVu12: object
        DejaVu18: object
        DejaVu24: object
        DejaVu40: object
        DejaVu56: object
        DejaVu72: object

class Board:
    """Board type enumeration."""
    UNKNOWN: int
    M5Stack: int
    M5StackCore2: int
    M5StickC: int
    M5StickCPlus: int
    M5Paper: int
    # Additional board types...

class Display:
    """Display interface for M5Stack devices."""
    
    def width(self) -> int:
        """Get display width in pixels."""
        ...
    
    def height(self) -> int:
        """Get display height in pixels."""
        ...
    
    def setBrightness(self, brightness: int) -> None:
        """Set display brightness (0-255)."""
        ...
    
    def setRotation(self, rotation: int) -> None:
        """Set display rotation (0-3)."""
        ...

def begin() -> None:
    """Initialize M5Stack hardware."""
    ...

def update() -> None:
    """Update button and touch states. Should be called regularly."""
    ...

def getBoard() -> int:
    """Get the current board type."""
    ...
