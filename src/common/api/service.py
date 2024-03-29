from typing import Iterable

import fastapi
import uvicorn
from facet import ServiceMixin

from .uvicorn_service import UvicornServer


class BaseAPIService(ServiceMixin):
    def __init__(
        self,
        title: str,
        version: str,
        root_url: str = "http://localhost",
        root_path: str = "",
        allowed_origins: Iterable[str] = (),
        port: int = 8000,
    ):
        self._title = title
        self._version = version
        self._root_url = root_url
        self._root_path = root_path
        self._allowed_origins = allowed_origins
        self._port = port

    def get_app(self) -> fastapi.FastAPI:
        app = fastapi.FastAPI(
            title=self._title,
            version=self._version,
            root_url=self._root_url,
            root_path=self._root_path,
        )
        app.service = self
        self.setup_app(app=app)

        return app

    def setup_app(self, app: fastapi.FastAPI):
        pass

    async def start(self):
        config = uvicorn.Config(app=self.get_app(), host="0.0.0.0", port=self._port)
        server = UvicornServer(config)

        self.add_task(server.serve())