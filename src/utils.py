from typing import List
from src.vacancy import Vacancy


def filter_vacancies_by_keyword(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    """
    Фильтрует вакансии по ключевому слову в описании.

    :param vacancies: Список вакансий
    :param keyword: Ключевое слово для фильтрации
    :return: Отфильтрованный список вакансий
    """
    return [vacancy for vacancy in vacancies if keyword.lower() in vacancy.description.lower()]


def filter_vacancies_by_salary(vacancies: List[Vacancy], min_salary: int) -> List[Vacancy]:
    """
    Фильтрует вакансии по минимальной зарплате.

    :param vacancies: Список вакансий
    :param min_salary: Минимальная зарплата
    :return: Отфильтрованный список вакансий
    """
    return [vacancy for vacancy in vacancies if vacancy._get_salary_value() >= min_salary]


def sort_vacancies(vacancies: List[Vacancy], reverse: bool = True) -> List[Vacancy]:
    """
    Сортирует вакансии по зарплате.

    :param vacancies: Список вакансий
    :param reverse: Сортировать по убыванию (по умолчанию True)
    :return: Отсортированный список вакансий
    """
    return sorted(vacancies, reverse=reverse)


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """
    Получает топ-N вакансий по зарплате.

    :param vacancies: Список вакансий
    :param top_n: Количество вакансий для вывода
    :return: Список топ-N вакансий
    """
    return vacancies[:top_n]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """
    Выводит вакансии в читаемом формате.

    :param vacancies: Список вакансий
    """
    for vacancy in vacancies:
        print(f"{vacancy.name} - {vacancy.salary} - {vacancy.url}")
