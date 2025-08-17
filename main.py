from fastapi import FastAPI

from models.pessoa_model import Pessoa
from dto.pessoa_create_dto import PessoaCreate
from repositories.pessoa_repository import PessoaRepository
from ssh import exec_ssh_command


app = FastAPI()

repo = PessoaRepository()


@app.get("/pessoas/")
def list_pessoas():
    return repo.get_all()


@app.post("/pessoa/")
def create_pessoa(pessoa: PessoaCreate):
    nova_pessoa = Pessoa(id=None, nome=pessoa.nome, idade=pessoa.idade)

    print(type(nova_pessoa.nome), nova_pessoa.nome)
    print(type(nova_pessoa.idade), nova_pessoa.idade)

    return repo.add(nova_pessoa)


@app.post("/exec_ssh")
def exec_ssh():
    exec_ssh_command()

    return {"mensagem": "Comando executado"}
