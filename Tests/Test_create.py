from multiprocessing.connection import Client

from API.api_client import ApiClient

dicta = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}
APIC = ApiClient()
APIC.get("/api/create", dicta)