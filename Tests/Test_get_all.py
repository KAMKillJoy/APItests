from API.api_client import ApiClient


def test_get_all():
    APIC = ApiClient()
    respall = APIC.get(f"/api/getAll")
    assert respall.status_code==200