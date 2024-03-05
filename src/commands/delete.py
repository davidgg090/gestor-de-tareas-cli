import click
from src.db.config import Session
from src.models.task import Task
from src.utils.notifications import send_notification


@click.command()
@click.argument('task_id', type=int)
def delete_task(task_id):
    session = Session()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            session.delete(task)
            session.commit()
            send_notification(f"Task '{task.name}' deleted.")
        else:
            send_notification(f"Task with id {task_id} not found.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar la tarea: {e}")
    finally:
        session.close()
