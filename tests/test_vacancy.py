import pytest
from src.vacancy import Vacancy

vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>",
                  "100 000-150 000 руб", "Требования: опыт работы от 3 лет...")


def test_init():
    assert vacancy.name == "Python Developer"
    assert vacancy.salary == "100 000-150 000 руб"
    assert vacancy.url == "<https://hh.ru/vacancy/123456>"
    assert vacancy.requirements == "Требования: опыт работы от 3 лет..."
    assert vacancy.salary_int_min == 100000


def test_str():
    assert str(vacancy) == 'Python Developer, 100 000-150 000 руб'
