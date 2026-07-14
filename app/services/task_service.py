from app.workflow.models.task import Task
from app.workflow.models.task_create import TaskCreate


class TaskService:
    """
    Handles all business logic related to tasks.
    """

    def create_task(self, task_data: TaskCreate) -> Task:
        return Task(
            title=task_data.title,
            description=task_data.description,
            priority=task_data.priority,
        )