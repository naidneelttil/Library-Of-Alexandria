from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ping")
def pong():
    return {"ping": "pong!"}
