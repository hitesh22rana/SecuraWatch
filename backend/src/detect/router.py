from fastapi import APIRouter, BackgroundTasks, Body

from src.detect.schemas import DetectIntrusionRequestSchema
from src.detect.service import DetectService
from src.responses import OK

router = APIRouter(
    tags=["Detect"],
    prefix="/detect",
)


@router.options("/intrusion", response_description="Detect intrusion")
async def intrusion_options():
    return OK(
        content=None,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type",
        },
    )


@router.post("/intrusion", response_description="Detect intrusion")
async def intrusion(
    background_tasks: BackgroundTasks,
    intrusion_details: DetectIntrusionRequestSchema = Body(...),
):
    return await DetectService().intrusion(
        background_tasks=background_tasks, intrusion_details=intrusion_details
    )
