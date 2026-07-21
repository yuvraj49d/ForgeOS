from app.execution.registry import ExecutorRegistry
from app.shared.logger import setup_logger
from app.workflow.context import WorkflowContext
from app.execution.models import ExecutionResult, ExecutionStatus

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
            try:
                executor = self.registry.get_executor(step.executor_type)
                result = executor.execute(step, context)

            except Exception as ex:
                logger.exception(
                    "Execution failed for step %d",
                    step.order,
                )

                result = ExecutionResult(
                    step_order=step.order,
                    executor=step.executor_type,
                    status=ExecutionStatus.FAILED,
                    error=str(ex),
                )

            context.execution_results.append(result)

        logger.info(
            "Execution completed for workflow %s",
            context.workflow_id,
        )