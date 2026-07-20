from datetime import UTC, datetime
from uuid import uuid4

from pydantic import BaseModel, Field

from app.agents.models.execution_plan import ExecutionPlan
from app.execution.models import ExecutionResult
from app.workflow.models.task import Task
from app.workflow.state import WorkflowState


class WorkflowContext(BaseModel):
    """
    Shared context for a single workflow execution.
    """

    workflow_id: str = Field(default_factory=lambda: str(uuid4()))

    task: Task

    state: WorkflowState = WorkflowState.CREATED

    execution_plan: ExecutionPlan | None = None

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    metadata: dict[str, str] = Field(default_factory=dict)

    execution_results: list[ExecutionResult] = Field(
        default_factory=list
    )