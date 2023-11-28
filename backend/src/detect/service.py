import subprocess

from fastapi import HTTPException, status

from src.detect.schemas import DetectIntrusionRequestSchema
from src.responses import OK
from src.storage_manager import storage_manager
from src.video_manager import video_manager


class DetectService:
    def __init__(self) -> None:
        pass

    async def intrusion(self, intrusion_details: DetectIntrusionRequestSchema):
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

            return OK(
                content={
                    "file_id": file_id,
                    "detail": "success: intrusion detected successfully",
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
