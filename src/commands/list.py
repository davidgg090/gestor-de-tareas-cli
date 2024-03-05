import click
from sqlalchemy.orm import Session
from src.db.config import Session
from src.models.task import Task, TaskStatus
from src.utils.notifications import send_notification


@click.command(name="list")
@click.option('--status', type=click.Choice([s.value for s in TaskStatus], case_sensitive=False),
              help="Filter tasks by status.")
def list_tasks(status):
    """Lists tasks based on the specified status filter.

    Args:
        status (str, optional): The status to filter tasks by.

    Returns:
        None
    """
    session = Session()
    try:
        query = session.query(Task)
        if status:
            query = query.filter(Task.status == TaskStatus[status.upper()])

        tasks = query.all()

        if tasks:
            for task in tasks:
                send_notification(
                    f"ID: {task.id}, Name: {task.name}, "
                    f"Description: {task.description}, "
                    f"Due Date: {task.due_date}, "
                    f"Priority: {task.priority}, "
                    f"Status: {task.status.value}")
        else:
            send_notification("No tasks found.")
    except Exception as e:
        send_notification(f"An error occurred: {e}")
    finally:
        session.close()