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
APIC = ApiClient()
resp = APIC.post("/api/create", **kwargs)
print (resp.status_code)
