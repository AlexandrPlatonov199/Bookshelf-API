import pytest

from src.books.authors.dao import AuthorDAO


@pytest.mark.parametrize(
    "first_name, last_name",
    [("Лев", "Толстой"), ("Михаил", "Булгаков"), ("Стивен", "Кинг")],
)
async def test_authors_find_one_or_none(first_name, last_name):
    authors = await AuthorDAO.find_one_or_none(
        first_name=first_name, last_name=last_name
    )

    assert authors.first_name == first_name
    assert authors.last_name == last_name
