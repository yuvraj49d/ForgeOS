from app.agents.models.execution_plan import PlanStep
from app.execution.base import BaseExecutor
from app.shared.logger import setup_logger
from app.workflow.context import WorkflowContext

logger = setup_logger()


class MockExecutor(BaseExecutor):

    def execute(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> None:

        logger.info(
            "Executing step %d - %s",
            step.order,
            step.title,
        )