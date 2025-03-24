import pytest
from unittest.mock import patch
from src.api import HeadHunterAPI


@pytest.fixture
def hh_api():
    return HeadHunterAPI()


@patch("src.api.requests.get")
def test_get_vacancies(mock_get, hh_api):
    """Тест получения вакансий с hh.ru"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": [
            {
                "name": "Любая вакансия",
                "alternate_url": "https://hh.ru/vacancy/999",
                "salary": {"from": 123456},
                "snippet": {"responsibility": "Пример обязанностей"}
            }
        ]
    }

    vacancies = hh_api.get_vacancies("Python")
    assert isinstance(vacancies, list)
    assert "name" in vacancies[0]
    assert "alternate_url" in vacancies[0]
    assert "salary" in vacancies[0]
    assert "snippet" in vacancies[0]
