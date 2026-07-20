from app.execution.base import BaseExecutor
from app.execution.executors.mock import MockExecutor


class ExecutorRegistry:
    """
    Registry for all executors.
    """

    def __init__(self):

        self.executors: dict[str, BaseExecutor] = {}

        self.register(
            "mock",
            MockExecutor(),
        )

    def register(
        self,
        executor_type: str,
        executor: BaseExecutor,
    ) -> None:

        self.executors[executor_type] = executor

    def get_executor(
        self,
        executor_type: str,
    ) -> BaseExecutor:

        executor = self.executors.get(executor_type)

        if executor is None:
            raise ValueError(
                f"No executor registered for '{executor_type}'."
            )

        return executor