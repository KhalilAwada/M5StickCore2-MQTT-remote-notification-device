#!/bin/bash

# M5Stack Core 2 Upload Script
# This script uploads Python files to your M5Stack Core 2 running UIFlow2 firmware

# Load .env file if it exists
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Configuration
PORT="${M5STACK_PORT:-/dev/ttyACM0}"
BAUD="${M5STACK_BAUD:-115200}"
FILE="${1:-main.py}"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}M5Stack Core 2 Upload Tool${NC}"
echo "================================"

# Check if file exists
if [ ! -f "$FILE" ]; then
    echo -e "${RED}Error: File '$FILE' not found${NC}"
    exit 1
fi

# Detect the port if not specified
if [ ! -e "$PORT" ]; then
    echo -e "${YELLOW}Port $PORT not found, searching for M5Stack...${NC}"
    
    # Common M5Stack ports
    for port in /dev/ttyUSB* /dev/ttyACM* /dev/cu.usbserial* /dev/cu.wchusbserial*; do
        if [ -e "$port" ]; then
            PORT="$port"
            echo -e "${GREEN}Found device at $PORT${NC}"
            break
        fi
    done
    
    if [ ! -e "$PORT" ]; then
        echo -e "${RED}Error: No M5Stack device found${NC}"
        echo "Please connect your M5Stack Core 2 and try again"
        exit 1
    fi
fi

echo "Port: $PORT"
echo "Baud Rate: $BAUD"
echo "File: $FILE"
echo "================================"

# Upload using mpremote (MicroPython remote control)
echo -e "${YELLOW}Uploading with mpremote...${NC}"
mpremote connect $PORT cp $FILE :/$FILE

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Upload successful!${NC}"
    echo ""
    echo "To run your code:"
    echo "  1. Press the reset button on your M5Stack"
    echo "  2. Or use: mpremote connect $PORT exec 'exec(open(\"$FILE\").read())'"
else
    echo -e "${RED}✗ Upload failed${NC}"
    echo ""
    echo "Troubleshooting:"
    echo "  - Ensure M5Stack is connected via USB"
    echo "  - Check that UIFlow2 firmware is installed"
    echo "  - Try a different USB cable or port"
    echo "  - Run: ls -l /dev/tty* to see available devices"
    echo "  - If in container, device may not be accessible - run ./upload-host.sh from Mac terminal"
    exit 1
fi
