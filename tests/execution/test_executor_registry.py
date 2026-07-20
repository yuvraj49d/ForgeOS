from app.execution.executors.mock import MockExecutor
from app.execution.registry import ExecutorRegistry


def test_registry_returns_mock_executor():
    registry = ExecutorRegistry()

    executor = registry.get_executor("mock")

    assert isinstance(executor, MockExecutor)