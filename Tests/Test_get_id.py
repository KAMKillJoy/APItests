from API.api_client import ApiClient


def test_get_id():
    APIC = ApiClient()
    id = 1
    resp = APIC.get(f"/api/get/{id}")
    assert resp.status_code==200