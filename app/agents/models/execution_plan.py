from typing import Any

from pydantic import BaseModel, Field


class PlanStep(BaseModel):
    """
    Represents one executable step.
    """

    order: int

    title: str

    description: str

    executor_type: str = "mock"

    inputs: dict[str, Any] = Field(default_factory=dict)

    expected_output: str | None = None


class ExecutionPlan(BaseModel):
    """
    Complete execution plan.
    """

    steps: list[PlanStep] = Field(default_factory=list)