from abc import ABC, abstractmethod

from app.agents.models.execution_plan import PlanStep
from app.execution.models import ExecutionResult, ExecutionStatus
from app.workflow.context import WorkflowContext


class BaseExecutor(ABC):
    """
    Base class for all executors.

    Implements the common execution lifecycle while allowing
    concrete executors to focus only on business logic.
    """

    def execute(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:
        """
        Standard execution pipeline.
        """

        self.validate(step)

        try:
            return self.execute_internal(step, context)

        except Exception as exc:
            return ExecutionResult(
                step_order=step.order,
                executor=step.executor_type,
                status=ExecutionStatus.FAILED,
                output=None,
                error=str(exc),
            )

    def validate(
        self,
        step: PlanStep,
    ) -> None:
        """
        Hook for executor-specific validation.

        Override this method if an executor needs to validate
        the incoming PlanStep before execution.
        """
        return

    @abstractmethod
    def execute_internal(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:
        """
        Executor-specific implementation.
        """
        raise NotImplementedError