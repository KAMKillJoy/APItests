from API.api_client import ApiClient

import json

# Открываем JSON-файл и загружаем его содержимое
with open('../Test_data/create.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

APIC = ApiClient()
APIC.get("/api/create", data)