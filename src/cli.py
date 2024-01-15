import typer

from . import (
    users,
)


def get_cli() -> typer.Typer:
    cli = typer.Typer()

    cli.add_typer(users.get_cli(), name="users")

    return cli