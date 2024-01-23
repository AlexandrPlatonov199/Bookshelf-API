import uuid

from pydantic import BaseModel, ConfigDict, NaiveDatetime


class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    description: str
    year_publication: int
    isbn: str
    number_page: int
    size: str
    cover_type: str
    age_restrictions: str
    created_at:NaiveDatetime
    updated_at:NaiveDatetime