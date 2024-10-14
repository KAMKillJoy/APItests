import allure

from API.api_client import ApiClient
import json
from models.create_model import EntityData

# Загрузка данных из JSON-файла
with open('../Test_data/create.json', 'r', encoding='utf-8') as file:
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

def test_create():
    allure.dynamic.title("Тест API-метода для создания новой сущности")
    allure.dynamic.description("Тест создаёт новую сущность, затем запрашивает её и убеждается в идентичности данных")
    allure.dynamic.tag("API_test", "Simbirsoft")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "John Doe")

    APIC = ApiClient()
    with allure.step("Отправка запроса на создание сущности"):respcr = APIC.post("/api/create", **kwargs)
    with allure.step("Проверка что код ответа 200"):assert respcr.status_code==200
    id2c = respcr.text
    respget = APIC.get(f"/api/get/{id2c}")
    with allure.step("Проверка соответствия содержимого additional_info ожидаемому"):
        assert json.loads(respget.text)["addition"]["additional_info"] == data["addition"]["additional_info"]
    with allure.step("Проверка соответствия содержимого additional_number ожидаемому"):
        assert json.loads(respget.text)["addition"]["additional_number"] == data["addition"]["additional_number"]
    with allure.step("Проверка соответствия содержимого title ожидаемому"):
        assert json.loads(respget.text)["title"] == data["title"]
    with allure.step("Проверка соответствия содержимого important_numbers ожидаемому"):
        assert json.loads(respget.text)["important_numbers"] == data["important_numbers"]