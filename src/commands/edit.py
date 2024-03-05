from datetime import datetime

import click
from src.db.config import Session
from src.models.task import Task, TaskStatus
from src.utils.notifications import send_notification


@click.command()
@click.argument('task_id', type=int)
@click.option('--name', type=str, help="The new name of the task.")
@click.option('--description', type=str, help="The new description of the task.")
@click.option('--due_date', type=str, help="The new due date of the task in format YYYY-MM-DD.")
@click.option('--priority', type=int, help="The new priority of the task.")
@click.option('--status', type=click.Choice([s.value for s in TaskStatus], case_sensitive=False), help="The new status of the task.")
def edit_task(task_id, name, description, due_date, priority, status):
    """Edits the specified task with new values for name, description, due date, priority, and status.

    Args:
        task_id (int): The ID of the task to edit.
        name (str, optional): The new name of the task.
        description (str, optional): The new description of the task.
        due_date (str, optional): The new due date of the task in format YYYY-MM-DD.
        priority (int, optional): The new priority of the task.
        status (str, optional): The new status of the task.

    Raises:
        ValueError: If the due date has an invalid format.

    Returns:
        None
    """
    session = Session()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            send_notification(f"Task with id {task_id} not found.")
            return

        if name:
            task.name = name
        if description:
            task.description = description
        if due_date:
            try:
                task.due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                send_notification("Invalid date format. Please use YYYY-MM-DD.")
                return
        if priority is not None:
            task.priority = priority
        if status:
            task.status = TaskStatus[status.upper()]

        session.commit()
        send_notification(f"Task '{task.name}' updated.")
    except Exception as e:
        send_notification(f"An error occurred: {e}")
    finally:
        session.close()
