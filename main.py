import click
from src.commands.add import add_task
from src.commands.delete import delete_task
from src.commands.edit import edit_task
from src.commands.list import list_tasks


@click.group(
    help="A CLI for managing tasks.",
)
def cli():
    pass


cli.add_command(add_task, name="add")

cli.add_command(delete_task, name="delete")

cli.add_command(edit_task, name="edit")

cli.add_command(list_tasks, name="list")

if __name__ == "__main__":
    cli()
