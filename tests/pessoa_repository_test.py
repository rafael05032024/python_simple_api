import unittest
from unittest.mock import MagicMock, patch
from repositories.pessoa_repository import PessoaRepository
from models.pessoa_model import Pessoa


class TestPessoaRepository(unittest.TestCase):

    @patch("repositories.pessoa_repository.get_connection")
    def setUp(self, mock_get_connection):
        # Cria mocks da conexão e cursor
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor

        # Faz get_connection() sempre retornar o mock_conn
        mock_get_connection.return_value = self.mock_conn

        # Agora instanciamos o repo normalmente
        self.repo = PessoaRepository()

    def test_add_pessoa(self):
        pessoa = Pessoa(id=None, nome="Maria", idade=30)

        # Configura o lastrowid simulado
        self.mock_cursor.lastrowid = 1

        result = self.repo.add(pessoa)

        self.assertEqual(result.id, 1)

    def test_get_pessoa(self):
        # Configura retorno do fetchone simulando tupla
        self.mock_cursor.fetchone.return_value = (1, "Maria", 30)

        pessoa = self.repo.get_pessoa(1)

        self.assertEqual(pessoa.id, 1)
        self.assertEqual(pessoa.nome, "Maria")
        self.assertEqual(pessoa.idade, 30)
