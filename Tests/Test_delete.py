import requests

from API.api_client import ApiClient
import json
import random

def test_delete():
    APIC = ApiClient()
    respall = APIC.get(f"/api/getAll")
    ids=[]
    for i in json.loads(respall.text)["entity"]:
        ids.append(i["id"])
    id2d = random.choice(ids)
    resp = APIC.delete(f"/api/delete/{id2d}")
    assert resp.status_code==204
    resp = requests.request("GET", APIC.base_url+"/api/get/"+f"{id2d}")
    assert resp.status_code == 500