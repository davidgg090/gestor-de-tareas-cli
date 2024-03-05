from datetime import datetime
import click

from app.db.config import Session
from app.models.task import Task, TaskStatus
from app.utils.notifications import send_notification


@click.command()
@click.argument("name", type=str, help="The name of the task.", required=True)
@click.argument("description", type=str, help="The description of the task.", required=True)
@click.option("--due_date", type=str, help="The due date of the task in the format YYYY-MM-DD.", required=False)
@click.option("--priority", type=int, help="The priority of the task.", required=False)
def add_task(name, description, due_date=None, priority=None):
    session = Session()
    try:
        if due_date:
            try:
                due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError as e:
                raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e
        if priority:
            try:
                priority = int(priority)
            except ValueError as exc:
                raise ValueError("Invalid priority. Must be an integer.") from exc
        task = Task(
            name=name,
            description=description,
            due_date=due_date_obj,
            priority=priority,
            status=TaskStatus.PENDING
        )
        session.add(task)
        session.commit()
        print(f"Task '{task.name}' added with id {task.id}")
        send_notification("added", f"Task '{task.name}' added with id {task.id}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    add_task("Test Task", "This is a test task.")
