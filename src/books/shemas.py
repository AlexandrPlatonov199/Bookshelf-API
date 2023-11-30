from pydantic import BaseModel, Field


class SBooks(BaseModel):
    author_id: int
    category_id: int
    name: str
    description: str
    year_publication: int
    isbn: str = Field(pattern=r"^\d{3}-\d-\d{2}-\d{6}-\d$")
    number_page: int
    size: str
    cover_type: str
    age_restrictions: str = Field(default="0+")
