from src.common.api.schemas import HealthResponse, ResponseStatus



async def health() -> HealthResponse:
    return HealthResponse(
        status=ResponseStatus.OK,
        version="0.0.0",
        name="users",
    )
