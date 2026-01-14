"""
Simple M5Stack Core 2 Test
Testing basic display functionality
"""

import M5
from M5 import Widgets
import time

# Initialize M5Stack
print("Initializing M5Stack...")
M5.begin()
print("M5 initialized")

# Try to set display
print("Setting up display...")
try:
    # Fill screen with a color to test if display works
    Widgets.fillScreen(0xFF0000)  # Red
    print("Screen filled with red")
    time.sleep(2)
    
    Widgets.fillScreen(0x00FF00)  # Green
    print("Screen filled with green")
    time.sleep(2)
    
    Widgets.fillScreen(0x0000FF)  # Blue
    print("Screen filled with blue")
    time.sleep(2)
    
    # Now try black background with text
    Widgets.fillScreen(0x000000)
    print("Screen cleared to black")
    
    # Simple text test
    Widgets.Label("Hello M5Stack!", 60, 100, 1.0, 0xFFFFFF, 0x000000, Widgets.FONTS.DejaVu24)
    print("Text displayed")
    
except Exception as e:
    print(f"Error: {e}")
    import sys
    sys.print_exception(e)

print("Test complete - check your M5Stack screen")
