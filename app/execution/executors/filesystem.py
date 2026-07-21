from enum import Enum
from pathlib import Path

from app.agents.models.execution_plan import PlanStep
from app.execution.base import BaseExecutor
from app.execution.models import ExecutionResult, ExecutionStatus
from app.workflow.context import WorkflowContext


class FileOperation(str, Enum):
    CREATE_FILE = "create_file"
    READ_FILE = "read_file"
    WRITE_FILE = "write_file"
    DELETE_FILE = "delete_file"
    LIST_DIRECTORY = "list_directory"


class FilesystemExecutor(BaseExecutor):

    def __init__(self):
        self._operations = {
            FileOperation.CREATE_FILE: self._create_file,
            FileOperation.READ_FILE: self._read_file,
            FileOperation.WRITE_FILE: self._write_file,
            FileOperation.DELETE_FILE: self._delete_file,
            FileOperation.LIST_DIRECTORY: self._list_directory,
        }

    def validate(
        self,
        step: PlanStep,
    ) -> None:

        operation = step.inputs.get("operation")
        path = step.inputs.get("path")

        if operation is None:
            raise ValueError("Missing 'operation'.")

        if path is None:
            raise ValueError("Missing 'path'.")

    def execute_internal(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:

        operation = FileOperation(step.inputs["operation"])

        handler = self._operations.get(operation)

        if handler is None:
            raise ValueError(f"Unsupported operation: {operation}")

        return handler(step, context)

    def _create_file(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:

        path = Path(step.inputs["path"])
        content = step.inputs.get("content", "")

        # Create parent directories if they don't exist
        path.parent.mkdir(parents=True, exist_ok=True)

        # Create/write the file
        path.write_text(content, encoding="utf-8")

        return ExecutionResult(
            step_order=step.order,
            executor=step.executor_type,
            status=ExecutionStatus.COMPLETED,
            output={
                "path": str(path),
                "created": True,
            },
            error=None,
        )

    def _read_file(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:

        path = Path(step.inputs["path"])

        if not path.exists():
            raise FileNotFoundError(
                f"File '{path}' does not exist."
            )

        content = path.read_text(
            encoding="utf-8",
        )

        return ExecutionResult(
            step_order=step.order,
            executor=step.executor_type,
            status=ExecutionStatus.COMPLETED,
            output={
                "path": str(path),
                "content": content,
            },
            error=None,
        )

    def _write_file(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:

        path = Path(step.inputs["path"])

        if not path.exists():
            raise FileNotFoundError(
                f"File '{path}' does not exist."
            )

        content = step.inputs.get("content", "")

        path.write_text(
            content,
            encoding="utf-8",
        )

        return ExecutionResult(
            step_order=step.order,
            executor=step.executor_type,
            status=ExecutionStatus.COMPLETED,
            output={
                "path": str(path),
                "written": True,
            },
            error=None,
        )

    def _delete_file(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:

        path = Path(step.inputs["path"])

        if not path.exists():
            raise FileNotFoundError(
                f"File '{path}' does not exist."
            )

        path.unlink()

        return ExecutionResult(
            step_order=step.order,
            executor=step.executor_type,
            status=ExecutionStatus.COMPLETED,
            output={
                "path": str(path),
                "deleted": True,
            },
            error=None,
        )

    def _list_directory(
        self,
        step: PlanStep,
        context: WorkflowContext,
    ) -> ExecutionResult:

        path = Path(step.inputs["path"])

        if not path.exists():
            raise FileNotFoundError(
                f"Directory '{path}' does not exist."
            )

        if not path.is_dir():
            raise NotADirectoryError(
                f"'{path}' is not a directory."
            )

        files = [
            item.name
            for item in path.iterdir()
        ]

        return ExecutionResult(
            step_order=step.order,
            executor=step.executor_type,
            status=ExecutionStatus.COMPLETED,
            output={
                "path": str(path),
                "files": files,
            },
            error=None,
        )