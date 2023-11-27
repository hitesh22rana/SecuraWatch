import aiofiles
from fastapi import File, HTTPException, UploadFile

from src.responses import Created
from src.storage import storage


class FileService:
    chunk_size_bytes: int = 1024 * 1024

    def __init__(self) -> None:
        pass

    async def upload(self, file: UploadFile = File(...)) -> Created | HTTPException:
        file_id = storage.generate_file_id()
        file_extension = storage.get_file_extension(file.filename)
        file_path = storage.get_file_path(
            file_id=file_id, file_extension=file_extension
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
            raise HTTPException(status_code=500, detail=str(e))
