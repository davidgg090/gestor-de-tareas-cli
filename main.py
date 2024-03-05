import click
from src.commands.add import add_task
from src.commands.delete import delete_task
from src.commands.edit import edit_task


@click.group()
def cli():
    pass


cli.add_command(add_task, name="add")

cli.add_command(delete_task, name="delete")

cli.add_command(edit_task, name="edit")

if __name__ == "__main__":
    cli()
