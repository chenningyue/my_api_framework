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