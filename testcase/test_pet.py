import time
import pytest
from api.pet_api import PetApi
from common.read_data import load_json

DATA = load_json("data/test_data.json")
@pytest.mark.smoke

@pytest.mark.parametrize("status",DATA["pet_status_cases"])
def test_find_by_status(status):
    api = PetApi()
    r = api.find_by_status(status)
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_pet():
    pet_id = int(time.time() * 1000)
    api = PetApi()
    r = api.create_pet(
        {"id": pet_id,
        "name": "doggie",
        "photoUrls": ["https://example.com/dog.jpg"],}
    )
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == pet_id
    api.delete_pet(pet_id)

def test_find_pet_by_id():
    pet_id = int(time.time() * 1000)
    api = PetApi()
    api.create_pet({"id": pet_id, "name": "doggie", "photoUrls": ["http://x.jpg"]})
    r = api.find_by_id(pet_id)  # 查
    assert r.status_code == 200
    assert r.json()["name"] == "doggie"
    api.delete_pet(pet_id)


def test_find_pet_by_notid():
    api = PetApi()
    r = api.find_by_id(18855484369)
    assert r.status_code == 404

def test_update_pet():
    pet_id = int(time.time() * 1000)
    api = PetApi()
    api.create_pet({"id": pet_id, "name": "doggie", "photoUrls": ["http://x.jpg"]})

    r = api.update_pet(
        {
            "id": pet_id,
            "name": "doggie2",
        }
    )
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "doggie2"
    api.delete_pet(pet_id)

def test_delete_pet():
    pet_id = int(time.time() * 1000)
    api = PetApi()
    api.create_pet({"id": pet_id, "name": "doggie", "photoUrls": ["http://x.jpg"]})
    r = api.delete_pet(pet_id)
    assert r.status_code == 200

def test_delete_pet_not_exist():
    api = PetApi()
    r = api.delete_pet(int(time.time() * 1000))
    assert r.status_code == 404
