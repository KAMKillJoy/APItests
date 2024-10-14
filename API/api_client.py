import os
import requests
import logging

# Настройка логирования
logger = logging.getLogger("api_client")
logging.basicConfig(level=logging.INFO)


class ApiClient:
    """
    Клиент для взаимодействия с API с использованием библиотеки requests.
    """

    def __init__(self):
        self.base_url = f"http://localhost:8080"  # Получение базового URL из переменной окружения

        # self.base_url = f"https://{os.getenv('RESOURCE_URL')}"  # Получение базового URL из переменной окружения

    def log_request(self, method: str, url: str, **kwargs):
        """
        Логирование отправляемых запросов.
        """
        logger.info(f"Отправка {method} запроса на {url} с параметрами: {kwargs}")

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Выполнение HTTP-запроса.
        """
        url = self.base_url + endpoint
        self.log_request(method, url, **kwargs)

        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()  # Проверка на ошибки
            return response
        except requests.exceptions.HTTPError as err:
            logger.error(f"HTTP ошибка: {err}")
            raise
        except Exception as e:
            logger.error(f"Ошибка при выполнении запроса: {e}")
            raise

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Выполнение GET-запроса.
        """
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Выполнение POST-запроса.
        """
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Выполнение PUT-запроса.
        """
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Выполнение DELETE-запроса.
        """
        return self.request("DELETE", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Выполнение PATCH-запроса.
        """
        return self.request("PATCH", endpoint, **kwargs)
