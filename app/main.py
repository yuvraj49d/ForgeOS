from fastapi import FastAPI

from app.configuration.settings import get_settings
from app.services.task_service import TaskService
from app.shared.logger import setup_logger
from app.middleware.request_logger import request_logging_middleware
from app.workflow.models.task import Task
from app.workflow.models.task import Task
from app.workflow.models.task_create import TaskCreate
from app.api.router import api_router

settings = get_settings()
logger = setup_logger()
task_service = TaskService()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.middleware("http")(request_logging_middleware)

@app.on_event("startup")
async def startup():
    logger.info("ForgeOS is starting...")

app.include_router(api_router)

