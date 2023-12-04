# Base image
FROM python:3.11-slim-buster

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /backend
WORKDIR /backend

# Copy the requirements.txt file
COPY ./requirements.txt /backend

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

# Copy the files and folder into the container
COPY ./src /backend/src
COPY ./src /backend/models

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the backend
CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000" ]