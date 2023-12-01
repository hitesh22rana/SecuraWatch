import subprocess

from fastapi import BackgroundTasks, HTTPException, status

from src.detect.background_tasks import intrusion_detection
from src.detect.schemas import DetectIntrusionRequestSchema
from src.responses import OK
from src.storage_service import storage_service
from src.video_service import video_service


class DetectService:
    def __init__(self) -> None:
        self.frames_batch_size: int = 5

    async def intrusion(
        self,
        background_tasks: BackgroundTasks,
        intrusion_details: DetectIntrusionRequestSchema,
    ):
        file_id: str = intrusion_details.file_id
        file_format: str = intrusion_details.file_format

        folder_path = storage_service.get_folder_path(file_id=file_id)
        input_path = folder_path + "/video." + file_format
        output_folder = folder_path + "/frames"
        storage_service.make_directory(output_folder, scratch=True)

        try:
            await video_service.video_to_image(
                input_path=input_path,
                fps=1,
                scale_x=640,
                scale_y=640,
                output_folder=output_folder,
                output_format="png",
            )

            frames: list[str] = storage_service.get_files(
                path=output_folder, type="png"
            )

            background_tasks.add_task(
                intrusion_detection,
                file_id=file_id,
                frames=frames,
                frames_batch_size=self.frames_batch_size,
                intrusion_type=intrusion_details.intrusion_type,
                recipient=intrusion_details.recipient,
            )

            return OK(
                content={
                    "file_id": file_id,
                    "detail": "success: added to intrusion detection queue",
                },
                headers={
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "POST",
                    "Access-Control-Allow-Headers": "Content-Type",
                },
            )

        except subprocess.CalledProcessError as e:
            raise HTTPException(
                status_code=500, detail="error: unable to convert video to images"
            ) from e

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="error: intrusion detection service unavailable",
            ) from e
