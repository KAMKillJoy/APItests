import random

import allure

from API.api_client import ApiClient
import json
from models.patch_model import  EntityData

# Загрузка данных из JSON-файла
with open('../Test_data/patch.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
# Создание экземпляра модели Pydantic с загруженными данными
entity_data = EntityData(**data)
# Сериализация данных в JSON
json_data = entity_data.model_dump_json()
# Подготовка kwargs с заголовками и данными
kwargs = {
    "headers": {
        "Content-Type": "application/json"
    },
    "data": json_data  # Передача сериализованных данных
}

def test_patch_id():
    allure.dynamic.title("Тест API-метода для изменения сущности")
    allure.dynamic.description("Тест изменяет сущность, затем убеждается что изменения соответствуют ожидаемым")
    allure.dynamic.tag("API_test", "Simbirsoft")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "John Doe")

    APIC = ApiClient()
    with allure.step("Выбор случайной сущности из существующих"):
        respall = APIC.get(f"/api/getAll")
        ids = []
        for i in json.loads(respall.text)["entity"]:
            ids.append(i["id"])
        id2p = random.choice(ids)
    with allure.step("Отправка запроса на изменение сущности"):resp = APIC.patch(f"/api/patch/{id2p}", **kwargs)
    with allure.step("Проверка что код ответа 204"):assert resp.status_code == 204
    respget = APIC.get(f"/api/get/{id2p}")
    with allure.step("Проверка соответствия содержимого additional_info ожидаемому"):
        assert json.loads(respget.text)["addition"]["additional_info"] == data["addition"]["additional_info"]
    with allure.step("Проверка соответствия содержимого additional_number ожидаемому"):
        assert json.loads(respget.text)["addition"]["additional_number"] == data["addition"]["additional_number"]
    with allure.step("Проверка соответствия содержимого title ожидаемому"):
        assert json.loads(respget.text)["title"] == data["title"]
    with allure.step("Проверка соответствия содержимого important_numbers ожидаемому"):
        assert json.loads(respget.text)["important_numbers"] == data["important_numbers"]
