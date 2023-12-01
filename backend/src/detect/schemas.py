from pydantic import BaseModel, Field


class DetectIntrusionRequestSchema(BaseModel):
    file_id: str = Field(..., description="File ID")
    file_format: str = Field(..., description="File format")
    intrusion_type: str = Field(..., description="Intrusion type")
    recipient: str = Field(..., description="Email")

    class Config:
        json_schema_extra = {
            "example": {
                "file_id": "file_id",
                "file_format": "file_format",
                "intrusion_type": "intrusion_type",
                "recipient": "recipient",
            }
        }
