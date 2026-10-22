import pytest
from api.store_api import StoreApi
from common.read_data import load_json
import time

@pytest.mark.smoke

def test_get_inventory():
    api = StoreApi()
    r = api.get_inventory()
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, dict)

def test_store_order():
    order_id = int(time.time() * 1000)
    api = StoreApi()
    r = api.create_order(
        {
            "id": order_id,
            "petId": 18855484368,
            "quantity": 0,
            "shipDate": "2026-10-22T13:38:37.440Z",
            "status": "placed",
            "complete": True
        }
    )
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == order_id
    api.delete_order(order_id)

def test_store_order_with_id():
    order_id = int(time.time() * 1000)
    api = StoreApi()
    api.create_order(
        {
            "id": order_id,
            "petId": 18855484368,
            "quantity": 0,
            "shipDate": "2026-10-22T13:38:37.440Z",
            "status": "placed",
            "complete": True
        }
    )
    r = api.get_order(order_id)
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == order_id
    api.delete_order(order_id)


def test_store_order_with_notid():
    api = StoreApi()
    r = api.get_order(int(time.time() * 1000))
    assert r.status_code == 404

def test_delete_order():
    order_id = int(time.time() * 1000)
    api = StoreApi()
    api.create_order(
        {
            "id": order_id,
            "petId": 18855484368,
            "quantity": 0,
            "shipDate": "2026-10-22T13:38:37.440Z",
            "status": "placed",
            "complete": True
        }
    )
    r = api.delete_order(order_id)
    assert r.status_code == 200
