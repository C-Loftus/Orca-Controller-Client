#!/bin/bash

if [ ! -f ~/.local/share/orca/orca-customizations.py ] || [ ! -s ~/.local/share/orca/orca-customizations.py ]; then
    cp src/orca-customizations.py ~/.local/share/orca/orca-customizations.py
    echo "Success"
    exit 0
else
    echo "ERROR installing you already have a file located at ~/.local/share/orca/orca-customizations.py that exists and is not empty"
    exit 1
fi