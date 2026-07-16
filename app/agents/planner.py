from app.agents.base import BaseAgent
from app.agents.models.execution_plan import (
    ExecutionPlan,
    PlanStep,
)
from app.workflow.context import WorkflowContext


class PlannerAgent(BaseAgent):

    def execute(
        self,
        context: WorkflowContext,
    ) -> ExecutionPlan:

        return ExecutionPlan(
            steps=[
                PlanStep(
                    order=1,
                    title="Analyze Task",
                    description="Understand user requirements.",
                ),
                PlanStep(
                    order=2,
                    title="Design Solution",
                    description="Prepare implementation strategy.",
                ),
                PlanStep(
                    order=3,
                    title="Execute",
                    description="Start implementation.",
                ),
            ]
        )