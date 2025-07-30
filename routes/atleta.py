from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional
from fastapi_pagination import Page, paginate
from models.atleta import Atleta
from schemas.atleta import AtletaListResponse, AtletaCreate
from database import get_db

router = APIRouter()

@router.get("/atletas", response_model=Page[AtletaListResponse])
def get_atletas(
    nome: Optional[str] = Query(None),
    cpf: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Atleta)
    if nome:
        query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Atleta.cpf == cpf)
    atletas = query.all()
    return paginate([
        AtletaListResponse(
            nome=a.nome,
            centro_treinamento=a.centro_treinamento.nome,
            categoria=a.categoria.nome
        ) for a in atletas
    ])

@router.post("/atletas")
def create_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    novo_atleta = Atleta(**atleta.dict())
    db.add(novo_atleta)
    try:
        db.commit()
        db.refresh(novo_atleta)
        return {"message": "Atleta criado com sucesso"}
    except IntegrityError as e:
        db.rollback()
        if "cpf" in str(e.orig):
            raise HTTPException(
                status_code=303,
                detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"
            )
        raise