from app.workflow.models.task import Task
from app.workflow.models.task_create import TaskCreate
from app.workflow.engine import WorkflowEngine

workflow_engine = WorkflowEngine()


class TaskService:
    """
    Handles all business logic related to tasks.
    """

    def create_task(self, task_data: TaskCreate) -> Task:
        task = Task(
            title=task_data.title,
            description=task_data.description,
            priority=task_data.priority,
        )

        workflow_engine.start(task)

        return task