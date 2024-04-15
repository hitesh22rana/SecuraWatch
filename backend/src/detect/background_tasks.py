from datetime import datetime

from src.config import settings
from src.detect.utils import isIntrusion, isWeapon
from src.email_service import email_service
from src.model_service import model_service
from src.storage_service import storage_service


def intrusion_detection(
    file_id: str,
    frames: list[str],
    frames_batch_size: int,
    min_confidence: float,
    intrusion_type: str,
    recipient: str,
):
    try:
        intrusion_detected: bool = False
        for index in range(0, len(frames), frames_batch_size):
            batch = frames[index : index + frames_batch_size]
            predictions = model_service.predict(batch)

            for prediction in predictions:
                if (
                    isIntrusion(prediction.class_label, intrusion_type)
                    and prediction.confidence > min_confidence
                ):
                    intrusion_detected = True
                    break

            if intrusion_detected:
                email_service.send_notification(
                    recipient=recipient,
                    title="Intrusion Detected - SecuraWatch",
                    subject=f"Intrusion Detected at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
                    message="We have detected an intrusion on your SecuraWatch surveillance system. Please find the video file attached for your reference.",
                    download_link=f"{settings.backend_api_url}/files/download/{file_id}",
                )
                break

        if not intrusion_detected:
            storage_service.delete_directory(file_id)

    except Exception as e:
        raise e


def threat_detection(
    file_id: str,
    frames: list[str],
    frames_batch_size: int,
    min_confidence: float,
    intrusion_type: str,
    recipient: str,
):
    try:
        intrusion_detected: bool = False
        weapon_detected: bool = False

        for index in range(0, len(frames), frames_batch_size):
            batch = frames[index : index + frames_batch_size]
            predictions = model_service.predict(batch)

            for prediction in predictions:
                if intrusion_detected and weapon_detected:
                    break

                if (
                    isIntrusion(prediction.class_label, intrusion_type)
                    and prediction.confidence > min_confidence
                ):
                    intrusion_detected = True

                if isWeapon(prediction.class_label) and prediction.confidence > (
                    min_confidence / 2
                ):
                    weapon_detected = True

            if intrusion_detected and weapon_detected:
                email_service.send_notification(
                    recipient=recipient,
                    title="Threat Detected - SecuraWatch",
                    subject=f"Threat Detected at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
                    message="We have detected a threat on your SecuraWatch surveillance system. Please find the video file attached for your reference.",
                    download_link=f"{settings.backend_api_url}/files/download/{file_id}",
                )
                break

        if not (intrusion_detected and weapon_detected):
            storage_service.delete_directory(file_id)

    except Exception as e:
        raise e
