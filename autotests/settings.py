import uuid

from pydantic import AnyHttpUrl, AnyUrl
from pydantic_settings import SettingsConfigDict, BaseSettings


class AutotestsSettings(BaseSettings):
    model_config = SettingsConfigDict(extra="allow", env_file=".env", secrets_dir="/run/secrets")

    users_base_url: AnyHttpUrl

    alexandr_id: uuid.UUID = uuid.UUID("03fe07b9-109c-4e11-a2a5-184921fbfc49")
    alexandr_email: str
