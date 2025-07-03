import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test task creation
def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Sample description"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"

# Test listing all tasks
def test_get_all_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test getting a task by ID
def test_get_task_by_id():
    # Create a new task to get its ID
    post_resp = client.post("/tasks/", json={"title": "Task for get"})
    task_id = post_resp.json()["id"]

    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == task_id

# Test updating a task
def test_update_task():
    # Create a task to update
    post_resp = client.post("/tasks/", json={"title": "To update"})
    task_id = post_resp.json()["id"]

    update_resp = client.put(f"/tasks/{task_id}", json={"title": "Updated Task", "is_completed": True})
    assert update_resp.status_code == 200
    assert update_resp.json()["title"] == "Updated Task"
    assert update_resp.json()["is_completed"] is True

# Test deleting a task
def test_delete_task():
    # Create a task to delete
    post_resp = client.post("/tasks/", json={"title": "To delete"})
    task_id = post_resp.json()["id"]

    del_resp = client.delete(f"/tasks/{task_id}")
    assert del_resp.status_code == 200

    # Check it's gone
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404
