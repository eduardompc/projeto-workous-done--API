from fastapi import FastAPI
from fastapi_pagination import add_pagination
from routes import atleta
from database import Base

app = FastAPI()
app.include_router(atleta.router)
add_pagination(app)