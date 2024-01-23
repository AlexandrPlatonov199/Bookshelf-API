from src.common.api.schemas.health import HealthResponse



async def health() -> HealthResponse:
    return HealthResponse(
        version="0.0.0",
        name="Users",
    )