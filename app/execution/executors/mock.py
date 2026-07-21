from app.execution.base import BaseExecutor
from app.agents.models.execution_plan import PlanStep
from app.execution.models import ExecutionResult, ExecutionStatus
from app.workflow.context import WorkflowContext


class MockExecutor(BaseExecutor):

    def execute_internal(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:

        return ExecutionResult(
            step_order=step.order,
            executor=step.executor_type,
            status=ExecutionStatus.COMPLETED,
            output={
                "message": "Mock execution completed successfully."
            },
            error=None,
        )