import pytest
from mock_app import app
from common.db import query

@pytest.mark.db
def test_students_api_matches_db():
    client = app.test_client()
    resp = client.get('/students')
    api_data = resp.get_json()

    db_data = query("SELECT id, name, class_name FROM students ORDER BY id")
    assert api_data == db_data