from fastapi import APIRouter, File, UploadFile

from src.files.service import FileService

router = APIRouter(
    tags=["Files"],
    prefix="/files",
)


@router.post("/upload", response_description="Upload file")
async def upload(file: UploadFile = File(...)):
    return await FileService().upload(file=file)


@router.get("/download/{file_id}", response_description="Download file")
async def download(file_id: str):
    return await FileService().download(file_id=file_id)
