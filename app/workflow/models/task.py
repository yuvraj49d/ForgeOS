from datetime import UTC, datetime
from uuid import uuid4

from pydantic import BaseModel, Field

from app.workflow.enums.priority import TaskPriority
from app.workflow.enums.status import TaskStatus


class Task(BaseModel):
    """
    Represents a task submitted to ForgeOS.
    """

    id: str = Field(default_factory=lambda: str(uuid4()))

    title: str = Field(..., min_length=3, max_length=100)

    description: str = Field(..., min_length=10)

    status: TaskStatus = TaskStatus.CREATED

    priority: TaskPriority = TaskPriority.MEDIUM

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )