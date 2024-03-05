from datetime import datetime
import click

from src.db.config import Session
from src.models.task import Task, TaskStatus
from src.utils.notifications import send_notification


@click.command()
@click.argument("name", type=str, required=True)
@click.argument("description", required=True)
@click.option("--due_date", type=str, help="The due date of the task in the format YYYY-MM-DD.", required=False)
@click.option("--priority", type=int, help="The priority of the task.", required=False)
def add_task(name, description, due_date=None, priority=None):
    """Adds a new task with the specified name, description, due date, and priority.

    Args:
        name (str): The name of the task.
        description (str): The description of the task.
        due_date (str, optional): The due date of the task in the format YYYY-MM-DD.
        priority (int, optional): The priority of the task.

    Raises:
        ValueError: If the due date has an invalid format or if the priority is not an integer.
        Exception: If an error occurs while adding the task.

    Returns:
        None
    """
    session = Session()
    try:
        if due_date:
            try:
                due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError as e:
                send_notification("An error occurred", f"Invalid date format. Please use YYYY-MM-DD. {e}")
        if priority:
            try:
                priority = int(priority)
            except ValueError as exc:
                send_notification("An error occurred", f"Invalid priority. Must be an integer. {exc}")
        task = Task(
            name=name,
            description=description,
            due_date=due_date_obj,
            priority=priority,
        )
        session.add(task)
        session.commit()
        send_notification(f"Task '{task.name}' added with id {task.id}")
    except Exception as e:
        send_notification(f"An error occurred: {e}")
    finally:
        session.close()

