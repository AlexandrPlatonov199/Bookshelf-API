from pydantic import BaseModel


class SAuthors(BaseModel):
    first_name: str
    last_name: str
