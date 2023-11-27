from fastapi import APIRouter, File, UploadFile

from src.files.service import FileService

router = APIRouter(
    tags=["Files"],
    prefix="/files",
)


@router.post("/upload", response_description="Upload file")
async def upload(file: UploadFile = File(...)):
    return await FileService().upload(file=file)
