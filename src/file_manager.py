from abc import ABC, abstractmethod
from typing import List
from src.vacancy import Vacancy
import json
import os

class AbstractFileManager(ABC):

    @abstractmethod
    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        pass

    @abstractmethod
    def load_vacancies(self) -> List[Vacancy]:
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass


class JSONFileManager(AbstractFileManager):
    def __init__(self, filename: str = "vacancies.json"):
        self._filename = filename

    def _read_file(self) -> List[dict]:
        if not os.path.exists(self._filename):
            return []
        with open(self._filename, "r", encoding="utf-8") as file:
            return json.load(file)

    def _write_file(self, data: List[dict]) -> None:
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        existing = self._read_file()
        existing_urls = {vac["url"] for vac in existing}
        new_vacancies = [v.to_dict() for v in vacancies if v.url not in existing_urls]
        self._write_file(existing + new_vacancies)

    def load_vacancies(self) -> List[Vacancy]:
        data = self._read_file()
        return [Vacancy(**item) for item in data]

    def add_vacancy(self, vacancy: Vacancy) -> None:
        self.save_vacancies([vacancy])

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        data = self._read_file()
        updated = [item for item in data if item["url"] != vacancy.url]
        self._write_file(updated)
