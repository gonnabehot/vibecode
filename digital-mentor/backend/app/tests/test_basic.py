from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_ask():
    r = client.post("/ask", json={"query": "Привет"})
    assert r.status_code == 200
    assert "answer" in r.json()
