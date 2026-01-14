"""SD Card Hardware Module Stub"""

from typing import Optional

class SDCard:
    """SD Card interface"""
    def __init__(
        self,
        slot: int = 2,
        width: int = 1,
        sck: int = 18,
        miso: int = 38,
        mosi: int = 23,
        cs: int = 4,
        freq: int = 1000000
    ) -> None:
        """Initialize SD card"""
        ...

__all__ = ['SDCard']
