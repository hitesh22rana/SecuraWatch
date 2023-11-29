import subprocess

from fastapi import HTTPException, status, BackgroundTasks

from src.detect.schemas import DetectIntrusionRequestSchema
from src.responses import OK
from src.storage_manager import storage_manager
from src.video_manager import video_manager
from src.detect.background_tasks import intrusion_detection


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

        folder_path = storage_manager.get_folder_path(file_id=file_id)
        input_path = folder_path + "/video." + file_format
        output_folder = folder_path + "/frames"
        storage_manager.make_directory(output_folder, scratch=True)

        try:
            await video_manager.video_to_image(
                input_path=input_path,
                fps=1,
                scale_x=640,
                scale_y=640,
                output_folder=output_folder,
                output_format="png",
            )

            frames: list[str] = storage_manager.get_files(
                path=output_folder, type="png"
            )

            background_tasks.add_task(
                intrusion_detection,
                file_id=file_id,
                frames=frames,
                frames_batch_size=self.frames_batch_size,
                intrusion_type=intrusion_details.intrusion_type,
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
