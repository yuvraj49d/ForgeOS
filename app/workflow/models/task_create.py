from pydantic import BaseModel, Field

from app.workflow.enums.priority import TaskPriority


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10)
    priority: TaskPriority = TaskPriority.MEDIUM