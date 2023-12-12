import pytest

from src.books.categorys.dao import CategoryDAO


@pytest.mark.parametrize("name", [("Драма"), ("Ужасы"), ("История")])
async def test_category_find_one_or_none(name):
    categorys = await CategoryDAO.find_one_or_none(name=name)

    assert categorys.name == name
