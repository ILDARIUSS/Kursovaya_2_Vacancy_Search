from typing import Optional
from dataclasses import dataclass

@dataclass
class Vacancy:
    """Класс для представления вакансии."""

    name: str
    url: str
    salary: Optional[str]
    description: str

    def __init__(self, name: str, url: str, salary: Optional[dict], description: str):
        """
        Инициализация вакансии.

        :param name: Название вакансии
        :param url: Ссылка на вакансию
        :param salary: Словарь с зарплатой (может быть None)
        :param description: Описание вакансии
        """
        self.name = name
        self.url = url
        self.salary = self._validate_salary(salary)
        self.description = description

    def _validate_salary(self, salary: Optional[dict]) -> str:
        """
        Валидация зарплаты. Если зарплата не указана, возвращает "Зарплата не указана".

        :param salary: Словарь с данными о зарплате или None
        :return: Строка с зарплатой
        """
        if salary and "from" in salary:
            return f"{salary['from']} руб."
        elif salary and "to" in salary:
            return f"до {salary['to']} руб."
        else:
            return "Зарплата не указана"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"Vacancy({self.name}, {self.salary}, {self.url})"

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (меньше)."""
        return self._get_salary_value() < other._get_salary_value()

    def __gt__(self, other: "Vacancy") -> bool:
        """Сравнение вакансий по зарплате (больше)."""
        return self._get_salary_value() > other._get_salary_value()

    def _get_salary_value(self) -> int:
        """
        Преобразует строковую зарплату в числовой формат для сравнения.

        :return: Число, соответствующее зарплате (0, если не указана)
        """
        if self.salary.startswith("Зарплата не указана"):
            return 0
        else:
            return int("".join(filter(str.isdigit, self.salary)))
