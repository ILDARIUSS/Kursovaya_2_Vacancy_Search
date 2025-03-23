from typing import Optional


class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ("name", "url", "salary", "description")

    def __init__(self, name: str, url: str, salary: Optional[dict], description: Optional[str]):
        self.name = name
        self.url = url
        self.salary = self._parse_salary(salary)
        self.description = description if isinstance(description, str) else "Описание отсутствует"

    def _parse_salary(self, salary: Optional[dict]) -> int:
        if salary and "from" in salary:
            return salary["from"]
        elif salary and "to" in salary:
            return salary["to"]
        return 0

    def __lt__(self, other: "Vacancy") -> bool:
        return self.salary < other.salary

    def __gt__(self, other: "Vacancy") -> bool:
        return self.salary > other.salary

    def __repr__(self) -> str:
        return f"Vacancy({self.name}, {self.salary} руб., {self.url})"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "description": self.description
        }
