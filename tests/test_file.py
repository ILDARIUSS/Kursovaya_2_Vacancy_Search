import pytest
import os
from src.file_manager import JSONFileManager
from src.vacancy import Vacancy

@pytest.fixture
def json_manager():
    """Фикстура для тестового JSON-файла"""
    manager = JSONFileManager("test_vacancies.json")
    yield manager
    os.remove("test_vacancies.json")  # Удаляем файл после тестов

def test_save_and_load(json_manager):
    """Тест сохранения и загрузки вакансий"""
    vacancy = Vacancy("Python Developer", "https://hh.ru/123", {"from": 150000}, "Требования...")
    json_manager.save_vacancies([vacancy])

    loaded_vacancies = json_manager.load_vacancies()
    assert len(loaded_vacancies) == 1
    assert loaded_vacancies[0].name == "Python Developer"

def test_add_and_delete(json_manager):
    """Тест добавления и удаления вакансий"""
    vacancy = Vacancy("Python Developer", "https://hh.ru/456", {"from": 100000}, "Django")

    json_manager.add_vacancy(vacancy)
    assert len(json_manager.load_vacancies()) == 1

    json_manager.delete_vacancy(vacancy)
    assert len(json_manager.load_vacancies()) == 0
