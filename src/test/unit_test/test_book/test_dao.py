import pytest

from src.books.dao import BookDAO


@pytest.mark.parametrize(
    "book_id, name",
    [(1, "Война и мир"), (2, "Кладбище домашних животных"), (3, "Мастер и Маргарита")],
)
async def test_book_find_one_or_none(book_id, name):
    result = await BookDAO.find_one_or_none(id=book_id, name=name)

    assert result.id == book_id
    assert result.name == name
