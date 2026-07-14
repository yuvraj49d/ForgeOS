from app.shared.logger import setup_logger
from app.workflow.context import WorkflowContext
from app.workflow.models.task import Task
from app.workflow.state import WorkflowState

logger = setup_logger()


class WorkflowEngine:
    """
    Executes and orchestrates a workflow.
    """

    def start(self, task: Task) -> WorkflowContext:
        context = WorkflowContext(task=task)

        logger.info(
            "Workflow %s created for task %s",
            context.workflow_id,
            task.id,
        )

        self._transition(context, WorkflowState.PLANNING)
        self._transition(context, WorkflowState.READY)
        self._transition(context, WorkflowState.COMPLETED)

        return context

    def _transition(
        self,
        context: WorkflowContext,
        new_state: WorkflowState,
    ) -> None:
        previous_state = context.state

        context.state = new_state

        logger.info(
            "Workflow %s transitioned: %s -> %s",
            context.workflow_id,
            previous_state,
            new_state,
        )