from abc import ABC, abstractmethod

from app.workflow.context import WorkflowContext


class BaseAgent(ABC):
    """
    Base class for every ForgeOS agent.
    """

    @abstractmethod
    def execute(self, context: WorkflowContext):
        pass