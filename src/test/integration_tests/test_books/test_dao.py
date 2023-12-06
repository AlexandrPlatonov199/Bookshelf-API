import pytest

from src.books.dao import BookDAO


@pytest.mark.parametrize("author_id,"
                         "category_id,"
                         "user_id,"
                         "name,"
                         "description,"
                         "year_publication,"
                         "isbn,"
                         "number_page,"
                         "size,"
                         "cover_type,"
                         "age_restrictions", [
    (1, 1, 1, "Идиот", "Про доброго человека", 2020, "978-5-38-921519-8", 300, "24x15", "Мягкий", "18+")
])
async def test_add_adn_get_book(author_id, category_id, user_id, name, description, year_publication, isbn,
                                number_page, size, cover_type, age_restrictions):
    book = await BookDAO.add(
        author_id=author_id,
        category_id=category_id,
        user_id=user_id,
        name=name,
        description=description,
        year_publication=year_publication,
        isbn=isbn,
        number_page=number_page,
        size=size,
        cover_type=cover_type,
        age_restrictions=age_restrictions,
    )

    assert book.author_id == author_id
    assert book.category_id == category_id
    assert book.user_id == user_id
    assert book.name == name
    assert book.description == description
    assert book.year_publication == year_publication
    assert book.isbn == isbn
    assert book.number_page == number_page
    assert book.size == size
    assert book.cover_type == cover_type
    assert book.age_restrictions == age_restrictions

    result = await BookDAO.find_one_or_none(id=book.id)

    assert result is not None 

