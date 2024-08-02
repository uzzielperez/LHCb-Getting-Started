#!/bin/bash

# Function to display a list of useful commands
function show_commands {
    echo "Useful Commands:"
    echo "----------------"
    echo "1. Activate environment: "
    echo "   source lhcbenv/bin/activate"
    echo "2. Increase Git buffer size to handle large pushes"
    echo " git config --global http.postBuffer 157286400"
    echo "3. Test image-coor.py"
    echo " cd detector" 
    echo " python image-coor.py"
}

# Run the function
show_commands