import allure
import requests

from API.api_client import ApiClient
import json
import random

def test_delete():
    allure.dynamic.title("Тест API-метода для удаления сущности")
    allure.dynamic.description("Тест удаляет сущность, "
                               "затем запрашивает её и убеждается что сервер вернул ошибку")
    allure.dynamic.tag("API_test", "Simbirsoft")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "John Doe")
    APIC = ApiClient()
    with allure.step("Выбор случайной сущности из существующих"):
        respall = APIC.get(f"/api/getAll")
        ids=[]
        for i in json.loads(respall.text)["entity"]:
            ids.append(i["id"])
        id2d = random.choice(ids)
    with allure.step("Удаление сущности"):resp = APIC.delete(f"/api/delete/{id2d}")
    with allure.step("Проверка что код ответа 204"):assert resp.status_code==204
    with allure.step("Запрос удалённой сущности"):
        resp = requests.request("GET", APIC.base_url+"/api/get/"+f"{id2d}")
    with allure.step("Проверка что код ответа 500, так как сущность не найдена"):assert resp.status_code == 500