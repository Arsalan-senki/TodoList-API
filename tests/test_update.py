from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_update_task_fields():
    post = client.post("/tasks/", json={"title": "Update Me"})
    task_id = post.json()["id"]

    put = client.put(f"/tasks/{task_id}", json={"title": "Updated Title", "is_completed": True})
    assert put.status_code == 200
    assert put.json()["title"] == "Updated Title"
    assert put.json()["is_completed"] is True

def test_partial_update_only_description():
    post = client.post("/tasks/", json={"title": "Partial"})
    task_id = post.json()["id"]

    put = client.put(f"/tasks/{task_id}", json={"description": "Just desc"})
    assert put.status_code == 200
    assert put.json()["description"] == "Just desc"
