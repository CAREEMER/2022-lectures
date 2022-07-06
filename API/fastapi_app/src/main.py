import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import auth, note, user
from core.config import app_config

# 09e7d55c-092c-4d26-b0e7-19affc650a74

app = FastAPI(
    title=f"Fastapi app - {app_config.ENVIRONMENT}",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    description="Sample FastAPI app",
)
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(user.router, prefix="/api/v1/user", tags=["user"])
app.include_router(note.router, prefix="/api/v1/note", tags=["note"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="0.0.0.0", port=8000, log_level=logging.DEBUG,
    )
