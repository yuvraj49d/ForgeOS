from app.agents.models.execution_plan import PlanStep
from app.execution.executors.filesystem import (
    FileOperation,
    FilesystemExecutor,
)
from app.execution.models import ExecutionStatus
from app.execution.types import ExecutorType
from app.workflow.context import WorkflowContext
from app.workflow.models.task import Task

def create_task() -> Task:
    return Task(
        title="Filesystem Test",
        description="Testing the filesystem executor.",
    )

def create_workflow_context() -> WorkflowContext:
    return WorkflowContext(
        task=create_task(),
    )

def create_plan_step(
    operation: FileOperation,
    path: str,
    content: str = "",
) -> PlanStep:
    return PlanStep(
        order=1,
        title=f"{operation.name.replace('_', ' ').title()}",
        description=f"Execute {operation.value} operation.",
        executor_type=ExecutorType.FILESYSTEM.value,
        inputs={
            "operation": operation.value,
            "path": path,
            "content": content,
        },
    )

def test_create_file(tmp_path):

    executor = FilesystemExecutor()
    context = create_workflow_context()

    file_path = tmp_path / "hello.txt"

    step = create_plan_step(
        FileOperation.CREATE_FILE,
        str(file_path),
        "Hello ForgeOS!",
    )

    result = executor.execute(step, context)

    assert result.status == ExecutionStatus.COMPLETED
    assert file_path.exists()
    assert file_path.read_text() == "Hello ForgeOS!"

def test_read_file(tmp_path):

    executor = FilesystemExecutor()
    context = create_workflow_context()

    file_path = tmp_path / "hello.txt"
    file_path.write_text("Hello ForgeOS!")

    step = create_plan_step(
        FileOperation.READ_FILE,
        str(file_path),
    )

    result = executor.execute(step, context)

    assert result.status == ExecutionStatus.COMPLETED
    assert result.output["content"] == "Hello ForgeOS!"

def test_write_file(tmp_path):

    executor = FilesystemExecutor()
    context = create_workflow_context()

    file_path = tmp_path / "hello.txt"
    file_path.write_text("Old Content")

    step = create_plan_step(
        FileOperation.WRITE_FILE,
        str(file_path),
        "New Content",
    )

    result = executor.execute(step, context)

    assert result.status == ExecutionStatus.COMPLETED
    assert file_path.read_text() == "New Content"

def test_delete_file(tmp_path):

    executor = FilesystemExecutor()
    context = create_workflow_context()

    file_path = tmp_path / "hello.txt"
    file_path.write_text("Delete me")

    step = create_plan_step(
        FileOperation.DELETE_FILE,
        str(file_path),
    )

    result = executor.execute(step, context)

    assert result.status == ExecutionStatus.COMPLETED
    assert not file_path.exists()

def test_list_directory(tmp_path):

    executor = FilesystemExecutor()
    context = create_workflow_context()

    (tmp_path / "a.txt").write_text("A")
    (tmp_path / "b.txt").write_text("B")

    step = create_plan_step(
        FileOperation.LIST_DIRECTORY,
        str(tmp_path),
    )

    result = executor.execute(step, context)

    assert result.status == ExecutionStatus.COMPLETED
    assert sorted(result.output["files"]) == [
        "a.txt",
        "b.txt",
    ]