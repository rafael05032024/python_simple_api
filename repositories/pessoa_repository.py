from models.pessoa_model import Pessoa
from database import get_connection


class PessoaRepository:

    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor(dictionary=True)

        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            idade INT
        )
        """)
        self.conn.commit()

    def add(self, pessoa: Pessoa):
        self.cursor.execute(
            "INSERT INTO pessoas (nome, idade) VALUES (%s, %s)",
            (pessoa.nome, pessoa.idade)
        )
        self.conn.commit()
        pessoa.id = self.cursor.lastrowid
        return pessoa

    def get_all(self):
        self.cursor.execute("SELECT id, nome, idade FROM pessoas")
        results = self.cursor.fetchall()
        return [Pessoa(**r) for r in results]

    def get_pessoa(self, pessoa_id: int):
        self.cursor.execute(
            "SELECT id, nome, idade FROM pessoas WHERE id = %s",
            (pessoa_id,)
        )
        row = self.cursor.fetchone()

        if row:
            # row = (id, nome, idade)
            return Pessoa(id=row[0], nome=row[1], idade=row[2])
        return None
