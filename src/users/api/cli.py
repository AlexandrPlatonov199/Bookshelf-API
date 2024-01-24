import asyncio

import typer

from src.users import database

from .service import get_service
from ..settings import UsersSettings


def run(ctx: typer.Context):
    settings: UsersSettings = ctx.obj["settings"]

    database_service = database.get_service(settings=settings)
    api_service = get_service(
        database=database_service,
        settings=settings,
    )

    asyncio.run(api_service.run())


def get_cli() -> typer.Typer:
    cli = typer.Typer()

    cli.command(name="run")(run)

    return cli
