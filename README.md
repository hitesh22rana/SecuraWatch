# SecuraWatch 🛡️

Vigilance Redefined, Security Reinvented

## About

SecuraWatch is a smart surveillance system built using Python, FastAPI, YOLOv8 deep learning model and Next.js. It allows users to monitor and detect intrusions through web cameras or phones. The system continuously captures video, processes them using a YOLOv8 model, and notifies users via email if a human is detected.

## Features

-   **Real-time Intrusion Detection:** The system continuously captures video in real-time and uses a YOLOv8 model for detecting human intrusions.

-   **Notification System:** Users receive email notifications with attached video clips whenever a human is detected.

-   **Web Dashboard:** View captured video clips and take appropriate actions through the web dashboard.

-   **Bulk Analysis:** Video clips are processed in bulk, reducing API load and improving efficiency.

## Getting Started

Follow these steps to set up and run SecuraWatch:

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/hitesh22rana/SecuraWatch.git
    cd SecuraWatch
    ```

2.  **Configuration:**

    Copy the .env.example file from the backend folder and paste your credentials.

    ```bash
    cp backend/.env.example backend/.env
    ```

    Update the .env file with your specific credentials.

3.  **Build and run the application**

    ```bash
    docker-compose -f docker-compose.yml up
    ```

## Acknowledgments

Special thanks to the creators of YOLO (You Only Look Once) for the powerful object detection model. [YOLOv8](https://github.com/ultralytics/ultralytics)
