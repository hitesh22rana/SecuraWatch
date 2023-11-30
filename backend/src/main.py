from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.detect.router import router as detect_router
from src.files.router import router as files_router

app = FastAPI(
    title="SecuraWatch",
    description="SecuraWatch: Vigilance Redefined, Security Reinvented",
    version="1.0.0",
)

"""Middleware"""
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
]

"""Routers"""
app.include_router(detect_router, prefix="/api/v1")
app.include_router(files_router, prefix="/api/v1")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        content={
            "status_code": "422",
            "detail": "Error: Unprocessable Entity",
        },
        status_code=422,
    )
