#!/bin/bash

# M5Stack Serial Monitor
# Press Ctrl+C to exit

PORT="${M5STACK_PORT:-/dev/tty.usbserial-58A70016771}"
BAUD="${M5STACK_BAUD:-115200}"

echo "M5Stack Serial Monitor"
echo "================================"
echo "Port: $PORT"
echo "Baud: $BAUD"
echo "Press Ctrl+] then Ctrl+C to exit"
echo "================================"
echo ""

# Use screen or pyserial miniterm
if command -v screen &> /dev/null; then
    screen "$PORT" "$BAUD"
else
    python3 -m serial.tools.miniterm "$PORT" "$BAUD" --eol LF
fi
