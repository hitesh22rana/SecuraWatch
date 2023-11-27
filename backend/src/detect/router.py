from fastapi import APIRouter

from src.detect.service import DetectService

router = APIRouter(
    tags=["Detect"],
    prefix="/detect",
)


@router.post("/intrusion/{file_id}", response_description="Detect intrusion")
async def intrusion(file_id: str):
    return DetectService().intrusion(file_id)
