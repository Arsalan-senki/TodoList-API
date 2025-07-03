from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task_success():
    response = client.post("/tasks/", json={"title": "New Task", "description": "Test"})
    assert response.status_code == 201
    assert response.json()["title"] == "New Task"

def test_create_task_missing_title():
    response = client.post("/tasks/", json={"description": "Missing title"})
    assert response.status_code == 422

def test_create_task_invalid_type():
    response = client.post("/tasks/", json={"title": 123})
    assert response.status_code == 422
