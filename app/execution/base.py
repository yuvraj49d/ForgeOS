from abc import ABC, abstractmethod

from app.agents.models.execution_plan import PlanStep
from app.workflow.context import WorkflowContext


class BaseExecutor(ABC):
    """
    Base class for every executor.
    """

    @abstractmethod
    def execute(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> None:
        """
        Execute a workflow step.
        """
        raise NotImplementedError