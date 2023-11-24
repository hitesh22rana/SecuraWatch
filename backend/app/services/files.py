# Purpose: File Service for handling files related operations.
# Path: backend\app\services\files.py

import os
from datetime import datetime
from uuid import uuid4

import aiofiles
from fastapi import File, HTTPException, UploadFile

from app.utils.responses import Created


class FileService:
    chunk_size_bytes: int = 1024 * 1024
    directory: str = "data"

    def __init__(self) -> None:
        if not os.path.exists(FileService.directory):
            os.makedirs(FileService.directory)

    def _get_file_extension(cls, file_name: str) -> str:
        indx: int = file_name.rfind(".")
        return file_name[indx:] if indx != -1 else ""

    def _generate_file_id(self) -> str:
        return str(datetime.now().strftime("%Y%m-%d%H-%M%S-") + str(uuid4()))

    def _get_file_path(self, file_id: str, file_extension: str) -> str:
        return f"{FileService.directory}/{file_id}.{file_extension}"

    async def upload(self, file: UploadFile = File(...)) -> Created | HTTPException:
        file_id = self._generate_file_id()
        file_extension = self._get_file_extension(file.filename)
        file_path = self._get_file_path(file_id=file_id, file_extension=file_extension)

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
