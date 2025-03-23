import os
import pytest
from src.file_manager import JSONFileManager
from src.vacancy import Vacancy


@pytest.fixture
def json_manager():
    """Фикстура для тестового JSON-файла"""
    filename = "test_vacancies.json"
    manager = JSONFileManager(filename)
    yield manager
    if os.path.exists(filename):
        os.remove(filename)


def test_save_and_load(json_manager):
    """Тест сохранения и загрузки вакансий"""
    vacancy = Vacancy("Python Developer", "https://hh.ru/123", {"from": 150000}, "Опыт работы с Django")
    json_manager.save_vacancies([vacancy])

    loaded = json_manager.load_vacancies()
    assert len(loaded) == 1
    assert loaded[0].name == "Python Developer"
    assert loaded[0].salary == 150000
    assert loaded[0].description == "Опыт работы с Django"


def test_add_and_delete(json_manager):
    """Тест добавления и удаления вакансии"""
    vacancy = Vacancy("Backend Dev", "https://hh.ru/456", {"from": 100000}, "REST API")

    json_manager.add_vacancy(vacancy)
    vacancies = json_manager.load_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0].url == "https://hh.ru/456"

    json_manager.delete_vacancy(vacancy)
    vacancies_after_delete = json_manager.load_vacancies()
    assert len(vacancies_after_delete) == 0
