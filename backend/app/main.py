# Purpose: Main file and entry point of the application
# Path: backend\app\main.py

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


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


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        content={
            "status_code": "422",
            "detail": "Error: Unprocessable Entity",
        },
        status_code=422,
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}
