from abc import ABC, abstractmethod

from app.agents.models.execution_plan import PlanStep
from app.execution.models import ExecutionResult
from app.workflow.context import WorkflowContext


class BaseExecutor(ABC):
    """
    Base class for all ForgeOS executors.
    """

    @abstractmethod
    def execute(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:
        """
        Execute a single workflow step.
        """
        raise NotImplementedError