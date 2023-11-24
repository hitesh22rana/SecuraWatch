#!/bin/bash

# Activate the virtual environment
source venv/Scripts/activate

# Check if isort is already installed
if ! pip3 show isort &>/dev/null; then
    echo "isort is not installed. Installing now..."
    pip3 install isort
fi

# Check if ruff is already installed
if ! pip3 show ruff &>/dev/null; then
    echo "ruff is not installed. Installing now..."
    pip3 install ruff
fi


# Run isort and ruff to format the Python code
isort . && ruff format .