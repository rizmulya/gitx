#!/bin/bash

if [[ "$OSTYPE" != "linux-gnu" ]]; then
    echo "For linux only"
    exit 1
fi

if ! command -v python3 &>/dev/null; then
    echo "This script requires Python"
    exit 1
fi

if [[ $EUID -ne 0 ]]; then
    echo "This script requires root privileges."
    exit 1
fi

if cp setup/gitx /usr/bin/ && cp gitx/ /usr/share/ -R; then
    echo "Installation completed successfully."
    echo ""
    echo "To set up your configuration file, run:"
    echo "------------------"
    echo "| sudo gitx edit |"
    echo "------------------"
fi
