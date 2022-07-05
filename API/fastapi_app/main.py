import logging

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import hr_data, measurement
from config import app_config


app = FastAPI(
    title="FastApi app",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    description=(f"Environment: {app_config.ENVIRONMENT}"),
)
app.include_router(measurement.router, prefix="/api/v1/", tags=["measurement"])
app.include_router(hr_data.router, prefix="/api-edg/v1/hr_data", tags=["hr_data"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="0.0.0.0", port=app_config.APP_PORT, log_level=logging.DEBUG,
    )
