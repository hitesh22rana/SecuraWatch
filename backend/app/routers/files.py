# Purpose: Files router for handling files related operations.
# Path: backend\app\routers\files.py

from fastapi import APIRouter, File, UploadFile

from app.services.files import FileService

router = APIRouter(
    tags=["Files"],
    prefix="/files",
)


@router.post("/upload", response_description="Upload file")
async def upload(file: UploadFile = File(...)):
    return await FileService().upload(file=file)
