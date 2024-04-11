# !/bin/bash

# check if .env file exists, if not exit
if [ ! -f .env ]; then
    echo "No .env file found, please create one, you can use the .env.example file as a template, exiting..."
    exit
fi

docker-compose -f docker-compose.yml up