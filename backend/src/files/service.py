import aiofiles
from fastapi import File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse

from src.responses import Created
from src.storage_service import storage_service


class FileService:
    chunk_size_bytes: int = 1024 * 1024

    def __init__(self) -> None:
        pass

    async def upload(self, file: UploadFile = File(...)) -> Created | HTTPException:
        file_id = storage_service.generate_file_id()
        file_extension = storage_service.get_file_extension(file.filename)
        storage_service.make_directory(directory=file_id, scratch=False)
        file_path = storage_service.get_file_path(
            file_id=f"{file_id}/video", file_extension=file_extension
        )

        try:
            async with aiofiles.open(file=file_path, mode="wb") as f:
                while chunk := await file.read(FileService.chunk_size_bytes):
                    await f.write(chunk)

            return Created(
                content={
                    "file_id": file_id,
                    "detail": "success: file uploaded successfully",
                },
                headers={
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "POST",
                    "Access-Control-Allow-Headers": "Content-Type",
                },
            )

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="error: files upload service unavailable",
            ) from e

    async def download(self, file_id: str) -> FileResponse | HTTPException:
        if not storage_service.validate_file_id(file_id=file_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="error: invalid file id",
            )

        return FileResponse(
            path=storage_service.get_file_path(
                file_id=f"{file_id}/video", file_extension=".webm"
            ),
            media_type="video/webm",
            filename=f"{file_id}.webm",
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "Content-Type",
                "Content-Disposition": f"attachment; filename={file_id}.webm",
                "Content-Type": "video/webm",
            },
        )
