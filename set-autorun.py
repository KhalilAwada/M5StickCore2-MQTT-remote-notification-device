#!/usr/bin/env python3
"""
Set M5Stack to auto-run main.py on boot
This sets boot_option to 0
"""

import time
from serial import Serial

PORT = "/dev/tty.usbserial-58A70016771"
BAUD = 115200

print("Setting M5Stack to auto-run mode...")
print(f"Port: {PORT}")

try:
    ser = Serial(PORT, BAUD, timeout=1)
    time.sleep(0.5)
    
    # Send Ctrl+C to interrupt any running program
    ser.write(b'\x03')
    time.sleep(0.2)
    
    # Enter raw REPL mode
    ser.write(b'\x01')
    time.sleep(0.2)
    
    # Read any existing data
    ser.read_all()
    
    # Execute command to set boot_option to 0
    cmd = b"""
import esp32
nvs = esp32.NVS("uiflow")
nvs.set_u8("boot_option", 0)
nvs.commit()
print("Boot option set to 0 (auto-run main.py)")
"""
    
    ser.write(cmd)
    ser.write(b'\x04')  # Ctrl+D to execute
    
    time.sleep(1)
    
    # Read response
    response = ser.read_all().decode('utf-8', errors='ignore')
    print(response)
    
    print("\n✓ Device configured to auto-run main.py on boot")
    print("Please reset your M5Stack (press the reset button)")
    
    ser.close()
    
except Exception as e:
    print(f"✗ Error: {e}")
    print("\nAlternative method:")
    print("1. Hold Button A on your M5Stack")
    print("2. While holding, press the Reset button")
    print("3. Release Button A when you see the menu")
    print("4. This will allow you to select 'Run main.py' option")
