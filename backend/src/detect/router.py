from fastapi import APIRouter, BackgroundTasks, Body

from src.detect.schemas import DetectIntrusionRequestSchema, DetectThreatRequestSchema
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


@router.post("/threat", response_description="Detect threat")
async def threat(
    background_tasks: BackgroundTasks,
    threat_details: DetectThreatRequestSchema = Body(...),
):
    return await DetectService().threat(
        background_tasks=background_tasks, threat_details=threat_details
    )
