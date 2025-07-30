# projeto workous done API
## Sobre o Projeto

Este projeto foi desenvolvido como parte do Bootcamp Santander promovido pela Digital Innovation One (DIO), com foco em APIs RESTful, FastAPI, SQLAlchemy e boas práticas de backend em Python.
Workouts API

## Funcionalidades

- **Filtros por nome e CPF nos endpoints de atleta:**  
  Utilize os parâmetros de query `nome` e `cpf` para filtrar atletas na listagem.

- **Resposta customizada para listagem de atletas:**  
  O endpoint de listagem retorna apenas `nome`, `centro de treinamento` e `categoria` de cada atleta.

- **Tratamento de exceção para CPF duplicado:**  
  Ao tentar cadastrar um atleta com CPF já existente, a API retorna status 303 e mensagem personalizada.

- **Paginação com fastapi-pagination:**  
  Todos os endpoints de listagem suportam paginação via parâmetros `limit` e `offset`.

## Exemplo de uso

### Listar atletas com filtros e paginação

```
GET /atletas?nome=João&cpf=12345678900&limit=10&offset=0
```

### Resposta esperada

```json
{
  "items": [
    {
      "nome": "João Silva",
      "centro_treinamento": "CT Zona Sul",
      "categoria": "Profissional"
    }
  ],
  "total": 1,
  "page": 1,
  "size": 10,
  "pages": 1
}
```

### Cadastro de atleta com tratamento de exceção

Se tentar cadastrar um atleta com CPF já existente:

```json
{
  "detail": "Já existe um atleta cadastrado com o cpf: 12345678900"
}
```

Status HTTP: `303`

---

## Instalação

1. Instale as dependências:
   ```
   pip install fastapi fastapi-pagination sqlalchemy uvicorn
   ```

2. Execute a aplicação:
   ```
   uvicorn main:app --reload
   ```

---

## Observações

- Certifique-se de que o banco de dados está configurado corretamente.
- Os endpoints seguem o padrão REST e retornam respostas em JSON.

Workouts API

## Funcionalidades

- Filtros por nome e CPF nos endpoints de atleta
- Resposta customizada para listagem de atletas (nome, centro de treinamento, categoria)
- Tratamento de exceção para CPF duplicado (status 303)
- Paginação com fastapi-pagination (limit, offset)