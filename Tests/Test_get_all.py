import allure

from API.api_client import ApiClient


def test_get_all():
    allure.dynamic.title("Тест API-метода для получения всех сущностей")
    allure.dynamic.description("Тест запрашивает все сущности и проверяет код 200")
    allure.dynamic.tag("API_test", "Simbirsoft")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    allure.dynamic.label("owner", "John Doe")

    APIC = ApiClient()
    with allure.step("Запрос всех сущностей"):respall = APIC.get(f"/api/getAll")
    with allure.step("Проверка что код ответа 200"):assert respall.status_code==200