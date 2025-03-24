from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API сервисов вакансий."""

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int = 20) -> list:
        """Получение списка вакансий по ключевому слову."""
        pass


class HeadHunterAPI(AbstractAPI):
    """Класс для работы с API hh.ru"""

    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        """Инициализация API клиента"""
        self._session = requests.Session()

    def _send_request(self, params: dict) -> dict:
        """Приватный метод отправки GET-запроса к API hh.ru"""
        response = self._session.get(self.BASE_URL, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Ошибка API hh.ru: {response.status_code}")

    def get_vacancies(self, keyword: str, per_page: int = 20) -> list:
        """
        Получение списка вакансий с hh.ru по ключевому слову.

        :param keyword: Ключевое слово для поиска вакансий
        :param per_page: Количество вакансий на странице (по умолчанию 20)
        :return: Список вакансий в формате словарей
        """
        params = {
            "text": keyword,
            "per_page": per_page
        }
        data = self._send_request(params)
        return data.get("items", [])
