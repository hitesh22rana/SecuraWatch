from datetime import datetime

from src.email_service import email_service
from src.model_service import model_service


def intrusion_detection(
    file_id: str,
    frames: list[str],
    frames_batch_size: int,
    intrusion_type: str,
    recipient: str,
):
    for index in range(0, len(frames), frames_batch_size):
        batch = frames[index : index + frames_batch_size]
        results = model_service.predict(batch)

        intrusion_detected: bool = False
        for result in results:
            if (
                len(result.boxes) != 0
                and result.names[result.boxes[0].cls[0].item()] == intrusion_type
            ):
                intrusion_detected = True
                break

        if intrusion_detected:
            email_service.send_notification(
                recipient=recipient,
                subject=f"Intrusion Detected at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
                download_link=f"http://127.0.0.1:8000/api/v1/files/download/{file_id}",
            )
            break
