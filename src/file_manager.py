import json
import os
from typing import List
from dataclasses import asdict
from src.vacancy import Vacancy

class JSONFileManager:
    """Класс для работы с JSON-файлом."""

    def __init__(self, filename: str = "vacancies.json"):
        self._filename = filename

    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        """Сохраняет список вакансий в JSON-файл."""
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump([asdict(vacancy) for vacancy in vacancies], file, ensure_ascii=False, indent=4)

    def load_vacancies(self) -> List[Vacancy]:
        """Загружает список вакансий из JSON-файла."""
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                vacancies_data = json.load(file)
                return [Vacancy(**data) for data in vacancies_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Добавляет вакансию в JSON-файл."""
        vacancies = self.load_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            self.save_vacancies(vacancies)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Удаляет вакансию из JSON-файла."""
        vacancies = self.load_vacancies()
        vacancies = [v for v in vacancies if v.url != vacancy.url]
        self.save_vacancies(vacancies)
