from fastapi import APIRouter, Body

from src.detect.service import DetectService
from src.detect.schemas import DetectIntrusionRequestSchema

router = APIRouter(
    tags=["Detect"],
    prefix="/detect",
)


@router.post("/intrusion", response_description="Detect intrusion")
async def intrusion(intrusion_details: DetectIntrusionRequestSchema = Body(...)):
    return await DetectService().intrusion(intrusion_details=intrusion_details)
