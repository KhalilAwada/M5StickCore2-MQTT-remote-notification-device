#!/bin/bash

# Upload image file to M5Stack flash memory
# Usage: ./upload-image.sh <image-file> [destination-name]

# Load .env file if it exists
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

PORT="${M5STACK_PORT:-/dev/tty.usbserial-58A70016771}"
IMAGE_FILE="$1"
DEST_NAME="${2:-$(basename $IMAGE_FILE)}"

if [ -z "$IMAGE_FILE" ]; then
    echo "Usage: ./upload-image.sh <image-file> [destination-name]"
    echo "Example: ./upload-image.sh github.png"
    exit 1
fi

if [ ! -f "$IMAGE_FILE" ]; then
    echo "Error: File '$IMAGE_FILE' not found"
    exit 1
fi

echo "Uploading image to M5Stack"
echo "================================"
echo "Port: $PORT"
echo "Source: $IMAGE_FILE"
echo "Destination: /flash/res/img/$DEST_NAME"
echo "================================"

# Check if ampy is installed
if ! command -v ampy &> /dev/null; then
    echo "Installing adafruit-ampy..."
    pip3 install adafruit-ampy
fi

# Create the directory structure first (ampy requires parent dirs to exist)
echo "Creating /flash/res/img directory..."
ampy --port "$PORT" mkdir /flash/res 2>/dev/null || true
ampy --port "$PORT" mkdir /flash/res/img 2>/dev/null || true

# Upload the image
ampy --port "$PORT" put "$IMAGE_FILE" "/flash/res/img/$DEST_NAME"

if [ $? -eq 0 ]; then
    echo "✓ Image uploaded successfully to /flash/res/img/$DEST_NAME"
else
    echo "✗ Upload failed"
    exit 1
fi
