from datetime import UTC, datetime
from uuid import uuid4

from pydantic import BaseModel, Field

from app.workflow.models.task import Task
from app.workflow.state import WorkflowState


class WorkflowContext(BaseModel):
    """
    Shared context for a single workflow execution.
    """

    workflow_id: str = Field(default_factory=lambda: str(uuid4()))

    task: Task

    state: WorkflowState = WorkflowState.CREATED

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    metadata: dict[str, str] = Field(default_factory=dict)