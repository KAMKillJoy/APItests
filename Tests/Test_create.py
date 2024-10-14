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
    APIC = ApiClient()
    respcr = APIC.post("/api/create", **kwargs)
    assert respcr.status_code==200
    id2c = respcr.text
    respget = APIC.get(f"/api/get/{id2c}")
    assert json.loads(respget.text)["addition"]["additional_info"] == data["addition"]["additional_info"]
    assert json.loads(respget.text)["addition"]["additional_number"] == data["addition"]["additional_number"]
    assert json.loads(respget.text)["title"] == data["title"]
    assert json.loads(respget.text)["important_numbers"] == data["important_numbers"]