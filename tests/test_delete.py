from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_delete_task_successfully():
    post = client.post("/tasks/", json={"title": "To Delete"})
    task_id = post.json()["id"]

    delete = client.delete(f"/tasks/{task_id}")
    assert delete.status_code in (200, 204)

    # Confirm deletion
    get = client.get(f"/tasks/{task_id}")
    assert get.status_code == 404
