from src.model_manager import model_manager


def intrusion_detection(
    file_id, frames: list[str], frames_batch_size: int, intrusion_type: str
):
    for i in range(0, len(frames), frames_batch_size):
        batch = frames[i : i + frames_batch_size]
        results = model_manager.predict(batch)

        for result in results:
            if result.names[result.boxes[0].cls[0].item()] == intrusion_type:
                print(f"intrusion detected: {file_id}")
