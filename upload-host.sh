#!/bin/bash

# This script runs on macOS host (outside container)
# It uses the container's Python files but accesses USB directly

# Load .env file if it exists
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

PORT="${M5STACK_PORT:-/dev/tty.usbserial-58A70016771}"
FILE="${1:-main.py}"

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
