# !/bin/bash

# check if .env file exists in backend and frontend folders
if [ ! -f backend/.env ]; then
    echo "No .env file found in backend folder, please create one, you can use the .env.example file as a template, exiting..."
    exit
fi

if [ ! -f frontend/.env ]; then
    echo "No .env file found, please create one, you can use the .env.example file as a template, exiting..."
    exit
fi

docker-compose -f docker-compose.yml up