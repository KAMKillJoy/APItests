import random

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
    APIC = ApiClient()

    respall = APIC.get(f"/api/getAll")
    ids = []
    for i in json.loads(respall.text)["entity"]:
        ids.append(i["id"])
    id2p = random.choice(ids)
    resp = APIC.patch(f"/api/patch/{id2p}", **kwargs)
    assert resp.status_code == 204
    respget = APIC.get(f"/api/get/{id2p}")
    assert json.loads(respget.text)["addition"]["additional_info"] == data["addition"]["additional_info"]
    assert json.loads(respget.text)["addition"]["additional_number"] == data["addition"]["additional_number"]
    assert json.loads(respget.text)["title"] == data["title"]
    assert json.loads(respget.text)["important_numbers"] == data["important_numbers"]
