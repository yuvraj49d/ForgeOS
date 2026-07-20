from app.agents.models.execution_plan import PlanStep
from app.execution.executors.mock import MockExecutor
from app.workflow.context import WorkflowContext
from app.workflow.models.task import Task


def test_mock_executor_returns_successful_result():
    executor = MockExecutor()

    task = Task(
        title="Test Task",
        description="Testing mock executor",
    )

    context = WorkflowContext(task=task)

    step = PlanStep(
        order=1,
        title="Mock Step",
        description="Mock execution",
        executor_type="mock",
    )

    result = executor.execute(
        step,
        context,
    )

    assert result.step_order == 1
    assert result.executor == "mock"

    # If you've already switched to ExecutionStatus:
    assert result.status.value == "completed"

    # Otherwise:
    # assert result.success is True

    assert result.error is None