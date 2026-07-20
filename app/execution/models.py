from datetime import datetime
from enum import Enum
from typing import Any
from datetime import UTC, datetime
from pydantic import BaseModel, Field


class ExecutionStatus(str, Enum):
    """
    Status of a workflow step execution.
    """

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class ExecutionResult(BaseModel):
    """
    Result of executing a single workflow step.
    """

    step_order: int

    executor: str

    status: ExecutionStatus

    output: Any | None = None

    error: str | None = None

    started_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )

    completed_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )