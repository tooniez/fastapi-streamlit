from fastapi.testclient import TestClient
from api.server import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from FastAPI"
    }  # Updated expected message


def test_demo_post():
    response = client.post("/demo_post", json={"data": "test"})
    assert response.status_code == 200
    assert response.json() == {"message": "Received data: test"}
