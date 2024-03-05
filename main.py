import click
from src.commands.add import add_task
from src.commands.delete import delete_task


@click.group()
def cli():
    pass


cli.add_command(add_task, name="add")

cli.add_command(delete_task, name="delete")


if __name__ == "__main__":
    cli()
