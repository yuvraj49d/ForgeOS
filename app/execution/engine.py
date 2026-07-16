from app.execution.registry import ExecutorRegistry
from app.shared.logger import setup_logger
from app.workflow.context import WorkflowContext

logger = setup_logger()


class ExecutionEngine:
    """
    Executes all steps in an execution plan.
    """

    def __init__(self):
        self.registry = ExecutorRegistry()

    def execute(
        self,
        context: WorkflowContext,
    ) -> None:

        if context.execution_plan is None:
            raise ValueError("Execution plan not found.")

        logger.info(
            "Starting execution of workflow %s",
            context.workflow_id,
        )

        for step in context.execution_plan.steps:

            logger.info(
                "Processing step %d",
                step.order,
            )

            executor = self.registry.get_executor(
                step.executor_type
            )

            executor.execute(
                step,
                context,
            )

        logger.info(
            "Execution completed for workflow %s",
            context.workflow_id,
        )