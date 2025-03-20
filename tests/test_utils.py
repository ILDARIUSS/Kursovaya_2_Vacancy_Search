import pytest
from src.utils import filter_vacancies_by_salary, filter_vacancies_by_keyword, sort_vacancies, get_top_vacancies
from src.vacancy import Vacancy


@pytest.fixture
def vacancies():
    return [
        Vacancy("Senior Python", "https://hh.ru/1", {"from": 200000}, "Django, Flask"),
        Vacancy("Middle Python", "https://hh.ru/2", {"from": 150000}, "FastAPI"),
        Vacancy("Junior Python", "https://hh.ru/3", {"from": 100000}, "Flask"),
    ]


def test_filter_vacancies_by_salary(vacancies):
    """Фильтрация по минимальной зарплате"""
    filtered = filter_vacancies_by_salary(vacancies, 150000)
    assert len(filtered) == 2  # Остаются Senior и Middle


def test_filter_vacancies_by_keyword(vacancies):
    """Фильтрация по ключевому слову"""
    filtered = filter_vacancies_by_keyword(vacancies, "Flask")
    assert len(filtered) == 2  # Остаются Senior и Junior


def test_sort_vacancies(vacancies):
    """Сортировка вакансий по зарплате"""
    sorted_vacs = sort_vacancies(vacancies)
    assert sorted_vacs[0].name == "Senior Python"
    assert sorted_vacs[-1].name == "Junior Python"


def test_get_top_vacancies(vacancies):
    """Получение топ-N вакансий"""
    top_vacs = get_top_vacancies(vacancies, 2)
    assert len(top_vacs) == 2
    assert top_vacs[0].name == "Senior Python"
