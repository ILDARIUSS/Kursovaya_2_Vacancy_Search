from src.vacancy import Vacancy


def test_vacancy_creation():
    """Тест создания вакансии и валидации зарплаты"""
    vacancy = Vacancy("Python Developer", "https://hh.ru/vacancy/12345", {"from": 100000}, "Опыт 3 года")

    assert vacancy.name == "Python Developer"
    assert vacancy.url == "https://hh.ru/vacancy/12345"
    assert vacancy.salary == 100000
    assert vacancy.description == "Опыт 3 года"


def test_salary_validation():
    """Проверка валидации, если зарплата отсутствует"""
    vacancy_no_salary = Vacancy("Python Dev", "https://hh.ru/vacancy/67890", None, "Нет опыта")
    assert vacancy_no_salary.salary == 0

    vacancy_to_only = Vacancy("Backend Dev", "https://hh.ru/789", {"to": 80000}, "REST API")
    assert vacancy_to_only.salary == 80000


def test_description_none():
    """Проверка замены None в description"""
    vacancy = Vacancy("Middle Dev", "https://hh.ru/555", {"from": 120000}, None)
    assert vacancy.description == "Описание отсутствует"


def test_vacancy_comparison():
    """Тест сравнения вакансий по зарплате"""
    vacancy1 = Vacancy("Senior", "https://hh.ru/1", {"from": 200000}, "...")
    vacancy2 = Vacancy("Junior", "https://hh.ru/2", {"from": 80000}, "...")

    assert vacancy1 > vacancy2
    assert not (vacancy1 < vacancy2)
