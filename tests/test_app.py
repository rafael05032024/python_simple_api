from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_criar_usuario():
    response = client.post("/usuarios/", json={"nome": "João", "email": "joao@email3"})
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "João"
    assert "id" in data