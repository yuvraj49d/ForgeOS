from fastapi import APIRouter

from app.configuration.settings import get_settings

router = APIRouter(tags=["Health"])

settings = get_settings()


@router.get("/")
async def health():
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "status": "healthy",
    }


@router.get("/ping")
async def ping():
    return {
        "message": "pong"
    }