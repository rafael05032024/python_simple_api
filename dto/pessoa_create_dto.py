from pydantic import BaseModel


class PessoaCreate(BaseModel):
    nome: str
    idade: int
