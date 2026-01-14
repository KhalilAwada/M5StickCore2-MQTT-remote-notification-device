"""Network module stub for MicroPython"""

from typing import Any, List, Tuple, Optional

# WiFi modes
STA_IF: int = 0  # Station (client) mode
AP_IF: int = 1   # Access Point mode

class WLAN:
    """WiFi network interface"""
    
    def __init__(self, interface_id: int) -> None:
        """
        Create WLAN network interface object
        Args:
            interface_id: STA_IF (0) for client mode, AP_IF (1) for access point
        """
        ...
    
    def active(self, is_active: Optional[bool] = None) -> bool:
        """Get or set interface active state"""
        ...
    
    def connect(self, ssid: str, password: str) -> None:
        """Connect to WiFi network"""
        ...
    
    def disconnect(self) -> None:
        """Disconnect from WiFi network"""
        ...
    
    def scan(self) -> List[Tuple[bytes, bytes, int, int, int, int]]:
        """
        Scan for available WiFi networks
        Returns: List of tuples (ssid, bssid, channel, RSSI, authmode, hidden)
        """
        ...
    
    def isconnected(self) -> bool:
        """Check if connected to WiFi"""
        ...
    
    def config(self, **kwargs: Any) -> Any:
        """
        Get or set network interface parameters
        Common params: dhcp_hostname, reconnects, ssid, password, etc.
        """
        ...
    
    def ifconfig(self, config: Optional[Tuple[str, str, str, str]] = None) -> Tuple[str, str, str, str]:
        """
        Get/set IP-level network interface parameters
        Returns/Sets: (ip, subnet, gateway, dns)
        """
        ...
    
    def status(self, param: Optional[str] = None) -> Any:
        """Query dynamic status information"""
        ...

__all__ = ['WLAN', 'STA_IF', 'AP_IF']
