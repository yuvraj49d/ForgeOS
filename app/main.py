from fastapi import FastAPI

from app.configuration.settings import get_settings
from app.shared.logger import setup_logger
from app.middleware.request_logger import request_logging_middleware

settings = get_settings()
logger = setup_logger()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.middleware("http")(request_logging_middleware)

@app.on_event("startup")
async def startup():
    logger.info("ForgeOS is starting...")


@app.get("/")
async def health():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "status": "healthy",
    }


@app.get("/ping")
async def ping():
    return {
        "message": "pong"
    }
