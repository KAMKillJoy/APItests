from API.api_client import ApiClient


def test_get_all():
    APIC = ApiClient()
    resp = APIC.get(f"/api/getAll")
    assert resp.status_code==200