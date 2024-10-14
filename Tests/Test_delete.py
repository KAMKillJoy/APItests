from API.api_client import ApiClient


def test_delete():
    APIC = ApiClient()
    id = 1
    resp = APIC.delete(f"/api/delete/{id}")
    assert resp.status_code==204