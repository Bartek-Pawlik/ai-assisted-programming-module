"""Route tests that monkeypatch Firestore helpers for isolated verification."""

from fastapi.testclient import TestClient
import pytest

from backend.app.main import app


@pytest.fixture()
def client() -> TestClient:
    return TestClient(app)


def test_health_check(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_notes(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    fake_notes = [
        {
            "id": "abc123",
            "title": "Grocery List",
            "content": "Milk, eggs, bread",
            "created_at": "2025-07-10T10:00:00Z",
        }
    ]

    monkeypatch.setattr("backend.app.firestore.list_notes", lambda: fake_notes)

    response = client.get("/notes")

    assert response.status_code == 200
    assert response.json() == fake_notes


def test_create_note(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_create(payload):
        data = payload.model_dump()
        return {"id": "new123", **data, "created_at": "2025-07-11T08:00:00Z"}

    monkeypatch.setattr("backend.app.firestore.create_note", fake_create)

    payload = {
        "title": "Meeting Notes",
        "content": "Discuss project timeline and deliverables",
    }

    response = client.post("/notes", json=payload)

    assert response.status_code == 201
    response_json = response.json()
    assert response_json["id"] == "new123"
    assert response_json["title"] == "Meeting Notes"
    assert response_json["content"] == "Discuss project timeline and deliverables"
    assert "created_at" in response_json


def test_delete_note(client: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    delete_called = {"count": 0}

    def fake_delete(note_id: str) -> None:
        delete_called["count"] += 1
        assert note_id == "abc123"

    monkeypatch.setattr("backend.app.firestore.delete_note", fake_delete)

    response = client.delete("/notes/abc123")

    assert response.status_code == 204
    assert delete_called["count"] == 1


def test_root_redirect(client: TestClient) -> None:
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/docs"

