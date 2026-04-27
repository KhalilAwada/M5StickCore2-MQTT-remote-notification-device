#!/bin/bash

# This script runs on the host (outside container) where the M5Stack is plugged in.
# Auto-detects the serial port on macOS and Linux. Override with M5STACK_PORT env
# or .env file.

# Load .env file if it exists
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Auto-detect serial port if M5STACK_PORT is not set
detect_port() {
    local candidates=()
    # macOS
    for p in /dev/tty.usbserial-* /dev/tty.SLAB_USBtoUART /dev/tty.wchusbserial*; do
        [ -e "$p" ] && candidates+=("$p")
    done
    # Linux
    for p in /dev/ttyUSB* /dev/ttyACM*; do
        [ -e "$p" ] && candidates+=("$p")
    done
    if [ ${#candidates[@]} -gt 0 ]; then
        echo "${candidates[0]}"
    fi
}

if [ -z "$M5STACK_PORT" ]; then
    M5STACK_PORT="$(detect_port)"
fi

PORT="$M5STACK_PORT"
FILE="${1:-main.py}"

if [ -z "$PORT" ] || [ ! -e "$PORT" ]; then
    echo "✗ No M5Stack serial port found."
    echo "  Plug in the device, or set M5STACK_PORT in .env (e.g. M5STACK_PORT=/dev/tty.usbserial-XXXX)."
    exit 1
fi

echo "M5Stack Upload (Host Mode)"
echo "================================"
echo "Port: $PORT"
echo "File: $FILE"
echo "================================"

# Check if ampy is installed on host
if ! command -v ampy &> /dev/null; then
    echo "Installing adafruit-ampy on host..."
    pip3 install adafruit-ampy
fi

# Upload the file
ampy --port "$PORT" put "$FILE"
if [ $? -eq 0 ]; then
    echo "✓ Upload successful!"
else
    echo "✗ Upload failed"
    exit 1
fi
