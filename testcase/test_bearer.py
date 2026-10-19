import pytest

from api.bearer_api import BearerApi
from common.read_data import load_json

DATA = load_json("data/test_data.json")
@pytest.mark.parametrize(
    "case",DATA["bearer_cases"],
    ids = [c["name"] for c in DATA["bearer_cases"]],
)
def test_bearer(case):
    api = BearerApi()
    r = api.bearer(case["token"])
    assert r.status_code == case["expect"]


