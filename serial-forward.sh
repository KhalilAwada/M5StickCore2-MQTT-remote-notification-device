#!/bin/bash
# Run this script on your Mac (not in container) to enable USB forwarding
# Install socat on Mac: brew install socat

PORT="${M5STACK_PORT:-/dev/tty.usbserial-58A70016771}"
FORWARD_PORT=5000

echo "Starting USB serial forwarding from Mac to container..."
echo "Device: $PORT"
echo "Forward: localhost:$FORWARD_PORT"
echo "Press Ctrl+C to stop"
echo ""

if ! command -v socat &> /dev/null; then
    echo "Installing socat..."
    brew install socat
fi

socat TCP-LISTEN:$FORWARD_PORT,reuseaddr,fork FILE:$PORT,b115200,raw,echo=0
