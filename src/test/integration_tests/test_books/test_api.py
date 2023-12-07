import pytest
from httpx import AsyncClient

from src.books.dao import BookDAO


@pytest.mark.parametrize(
    "author_id,"
    "category_id,"
    "user_id,"
    "name,"
    "description,"
    "year_publication,"
    "isbn,"
    "number_page,"
    "size,"
    "cover_type,"
    "age_restrictions,"
    "status_cod",
    [
        (
            1,
            1,
            1,
            "Идиот",
            "Про доброго человека",
            2020,
            "978-5-38-921519-2",
            300,
            "24x15",
            "Мягкий",
            "18+",
            200,
        )
    ],
)
async def test_authenticated_ac_add_book(
    authenticated_ac: AsyncClient,
    author_id,
    category_id,
    user_id,
    name,
    description,
    year_publication,
    isbn,
    number_page,
    size,
    cover_type,
    age_restrictions,
    status_cod,
):
    response = await authenticated_ac.post(
        "/books",
        json={
            "author_id": author_id,
            "category_id": category_id,
            "user_id": user_id,
            "name": name,
            "description": description,
            "year_publication": year_publication,
            "isbn": isbn,
            "number_page": number_page,
            "size": size,
            "cover_type": cover_type,
            "age_restrictions": age_restrictions,
        },
    )

    assert response.status_code == status_cod

    result = await BookDAO.find_one_or_none(name=name)

    assert result is not None
