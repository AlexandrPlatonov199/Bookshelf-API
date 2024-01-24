import asyncio

import typer

from src.users import database

from .service import get_service


def serve(ctx: typer.Context):
    settings = ctx.obj["settings"]

    database_service = database.get_service(settings=settings)
    users_service = get_service(
        database=database_service,
        settings=settings,
    )

    asyncio.run(users_service.run())


def get_cli() -> typer.Typer:
    cli = typer.Typer()

    cli.command(name="serve")(serve)

    return cli