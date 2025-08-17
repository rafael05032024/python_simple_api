from dataclasses import dataclass


@dataclass
class Pessoa:
    id: int | None
    nome: str
    idade: int
