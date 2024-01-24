import typer

from . import (
    users,
    books,
)


def get_cli() -> typer.Typer:
    cli = typer.Typer()

    cli.add_typer(users.get_cli(), name="users")
    cli.add_typer(books.get_cli(), name="books")

    return cli