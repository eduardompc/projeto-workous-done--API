from pydantic import BaseModel

class AtletaListResponse(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str

    class Config:
        orm_mode = True

class AtletaCreate(BaseModel):
    nome: str
    cpf: str
    centro_treinamento_id: int
    categoria_id: int