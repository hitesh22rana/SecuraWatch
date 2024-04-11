#!/bin/bash

# Check if ffmpeg is installed on the system, exit if not
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found, please install it on your system, you can download it from https://ffmpeg.org/download.html, exiting..."
    exit
fi

# Navigate to the /backend directory
cd backend/

# Activate the virtual environment
if [[ "$OSTYPE" == "mswin" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" || "$OSTYPE" == "win64" || "$OSTYPE" == "msys" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# check if .env file exists, if not exit
if [ ! -f .env ]; then
    echo "No .env file found, please create one, you can use the .env.example file as a template, exiting..."
    exit
fi

# Run the api
uvicorn src.main:app --reload