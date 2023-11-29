from fastapi import APIRouter, Body, BackgroundTasks

from src.detect.schemas import DetectIntrusionRequestSchema
from src.detect.service import DetectService

router = APIRouter(
    tags=["Detect"],
    prefix="/detect",
)


@router.post("/intrusion", response_description="Detect intrusion")
async def intrusion(
    background_tasks: BackgroundTasks,
    intrusion_details: DetectIntrusionRequestSchema = Body(...),
):
    return await DetectService().intrusion(
        background_tasks=background_tasks, intrusion_details=intrusion_details
    )
