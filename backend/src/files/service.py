import aiofiles
from fastapi import File, HTTPException, UploadFile, status

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
