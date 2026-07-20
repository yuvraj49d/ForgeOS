from app.workflow.engine import WorkflowEngine
from app.workflow.models.task import Task
from app.workflow.state import WorkflowState


def test_workflow_engine_completes_workflow():
    engine = WorkflowEngine()

    task = Task(
        title="Test Workflow",
        description="Testing workflow execution",
    )

    context = engine.start(task)

    assert context.task == task
    assert context.execution_plan is not None
    assert len(context.execution_results) > 0
    assert context.state == WorkflowState.COMPLETED