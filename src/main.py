from fastapi import Depends, FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ping")
def pong():
    return {"ping": "pong!"}
