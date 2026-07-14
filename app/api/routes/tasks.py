from fastapi import APIRouter

from app.services.task_service import TaskService
from app.workflow.models.task import Task
from app.workflow.models.task_create import TaskCreate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

task_service = TaskService()


@router.post("", response_model=Task)
async def create_task(task: TaskCreate):

    return task_service.create_task(task)