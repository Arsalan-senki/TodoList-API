from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_task_by_id():
    post = client.post("/tasks/", json={"title": "Fetch Me"})
    assert post.status_code == 201
    task_id = post.json()["id"]

    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == task_id
