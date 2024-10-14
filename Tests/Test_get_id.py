import json
import random
import allure
from API.api_client import ApiClient


def test_get_id():
    allure.dynamic.title("Тест API-метода для получения сущности по id")
    allure.dynamic.description("Тест запрашивает сущность по id и проверяет код 200")
    allure.dynamic.tag("API_test", "Simbirsoft")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "John Doe")
    APIC = ApiClient()
    with allure.step("Выбор случайной сущности из существующих"):
        respall = APIC.get(f"/api/getAll")
        ids = []
        for i in json.loads(respall.text)["entity"]:
            ids.append(i["id"])
        id2g = random.choice(ids)
    with allure.step("Запрос сущности"):resp = APIC.get(f"/api/get/{id2g}")
    with allure.step("Проверка что код ответа 200"):assert resp.status_code==200