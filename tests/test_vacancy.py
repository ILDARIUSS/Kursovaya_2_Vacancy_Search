import pytest
from src.vacancy import Vacancy


def test_vacancy_creation():
    """Тест создания вакансии и валидации зарплаты"""
    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/12345", {"from": 100000}, "Опыт 3 года")

    assert vacancy.name == "Python Developer"
    assert vacancy.url == "https://hh.ru/vacancy/12345"
    assert vacancy.salary == "100000 руб."
    assert vacancy.description == "Опыт 3 года"


def test_salary_validation():
    """Тест валидации зарплаты"""
    vacancy_no_salary = Vacancy("Python Dev", "https://hh.ru/vacancy/67890", None, "Нет опыта")
    assert vacancy_no_salary.salary == "Зарплата не указана"

    vacancy_to_salary = Vacancy("Middle Python", "https://hh.ru/vacancy/54321", {"to": 120000}, "Django")
    assert vacancy_to_salary.salary == "до 120000 руб."


def test_vacancy_comparison():
    """Тест сравнения вакансий по зарплате"""
    vacancy1 = Vacancy("Python Dev", "https://hh.ru/1", {"from": 100000}, "...")
    vacancy2 = Vacancy("Junior Python", "https://hh.ru/2", {"to": 80000}, "...")

    assert vacancy1 > vacancy2
    assert not (vacancy1 < vacancy2)
