#!/usr/bin/env python3
"""
Test running main.py on M5Stack and capture any errors
"""

import time
from serial import Serial

PORT = "/dev/tty.usbserial-58A70016771"
BAUD = 115200

print("Testing main.py on M5Stack...")
print(f"Port: {PORT}\n")

try:
    ser = Serial(PORT, BAUD, timeout=2)
    time.sleep(0.5)
    
    # Send Ctrl+C to stop any running program
    ser.write(b'\x03\x03')
    time.sleep(0.3)
    ser.read_all()
    
    # Send command to run main.py
    print("Running: execfile('/flash/main.py')\n")
    ser.write(b"execfile('/flash/main.py')\r\n")
    
    # Wait and capture output
    time.sleep(5)
    response = ser.read_all().decode('utf-8', errors='ignore')
    
    if response.strip():
        print("Device Output:")
        print("=" * 50)
        print(response)
        print("=" * 50)
        
        # Check for errors
        if "Traceback" in response or "Error" in response:
            print("\n⚠️  Errors detected in output above")
        else:
            print("\n✓ No errors detected")
            print("If screen is still black, the issue might be:")
            print("  - Display initialization")
            print("  - Widget/GUI API differences")
            print("  - Code is running but display not updating")
    else:
        print("No output received - code may be running silently")
        print("Check your M5Stack screen for visual output")
    
    ser.close()
    
except Exception as e:
    print(f"✗ Error: {e}")
