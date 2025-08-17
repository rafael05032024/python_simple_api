import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestAPI(unittest.TestCase):

    @patch("main.repo")
    def test_list_pessoas(self, mock_repo):
        mock_repo.get_all.return_value = [
            {"id": 1, "nome": "Maria", "idade": 30}
        ]

        response = client.get("/pessoas/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id": 1, "nome": "Maria",
                                            "idade": 30}])

    @patch("main.repo")
    def test_create_pessoa(self, mock_repo):
        mock_repo.add.return_value = {"id": 1, "nome": "João", "idade": 25}

        payload = {"nome": "João", "idade": 25}
        response = client.post("/pessoa/", json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 1, "nome": "João",
                                           "idade": 25})

    @patch("main.exec_ssh_command")
    def test_exec_ssh(self, mock_exec_ssh):
        response = client.post("/exec_ssh")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"mensagem": "Comando executado"})
        mock_exec_ssh.assert_called_once()
