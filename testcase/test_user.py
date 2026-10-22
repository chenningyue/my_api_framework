import pytest
from api.user_api import UserApi
from common.read_data import load_json
import time

@pytest.mark.smoke

def test_create_user():
    username = int(time.time() * 1000)
    api = UserApi()
    r = api.create_user({"username":username,"password":"cny"})
    assert r.status_code == 200
    api.delete_user(username)

def test_find_user():
    username = int(time.time() * 1000)
    api = UserApi()
    api.create_user({"username":username,"password":"cny"})
    r = api.get_user(username)
    assert r.status_code == 200
    data = r.json()
    assert data["username"] == str(username)
    api.delete_user(username)


def test_find_notuser():
    api = UserApi()
    r = api.get_user(f"no_such_{int(time.time() * 1000)}")  
    assert r.status_code == 404

def test_update_user():
    username = int(time.time() * 1000)
    api = UserApi()
    api.create_user({"username":username,"password":"cny"})
    r = api.update_user(username,
                        {"id": 0,
      "username": "cny2",
      "firstName": "cny2",
      "lastName": "cny2",
      "email": "cny2",
      "password": "cny2",
      "phone": "cny2",
      "userStatus": 0}
                         )
    assert r.status_code == 200
    api.delete_user(username)

def test_delete_user():
    username = int(time.time() * 1000)
    api = UserApi()
    api.create_user({"username":username,"password":"cny"})

    r = api.delete_user(username)
    assert r.status_code == 200
    api.delete_user(username)

def test_login_user():
    api = UserApi()
    r = api.login_user("cny","cny")
    assert r.status_code == 200
    assert "message" in r.text
