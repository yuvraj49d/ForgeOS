from app.agents.models.execution_plan import PlanStep
from app.execution.base import BaseExecutor
from app.execution.models import ExecutionResult, ExecutionStatus
from app.shared.logger import setup_logger
from app.workflow.context import WorkflowContext

logger = setup_logger()


class MockExecutor(BaseExecutor):
    """
    Mock executor used during development.
    """

    def execute(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:

        logger.info(
            "Executing step %d - %s",
            step.order,
            step.title,
        )

        return ExecutionResult(
            step_order=step.order,
            executor="mock",
            status=ExecutionStatus.COMPLETED,
            output=f"Successfully executed '{step.title}'",
        )