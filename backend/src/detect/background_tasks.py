from src.model_service import model_service


def intrusion_detection(
    file_id, frames: list[str], frames_batch_size: int, intrusion_type: str
):
    for index in range(0, len(frames), frames_batch_size):
        batch = frames[index : index + frames_batch_size]
        results = model_service.predict(batch)

        for result in results:
            if result.names[result.boxes[0].cls[0].item()] == intrusion_type:
                print(f"intrusion detected: {file_id}")
