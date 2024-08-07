#!/bin/bash

input_file="./res/main.ui"
output_file="./main_ui.py"

pyuic5 $input_file -o $output_file

if [ $? -eq 0 ]; then
    echo "Conversion successful: $input_file -> $output_file"
else
    echo "Conversion failed."
fi
