from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_nonexistent_task():
    response = client.get("/tasks/999999")
    assert response.status_code == 404

def test_update_nonexistent_task():
    response = client.put("/tasks/999999", json={"title": "Doesn't exist"})
    assert response.status_code == 400

def test_delete_nonexistent_task():
    response = client.delete("/tasks/999999")
    assert response.status_code == 400
