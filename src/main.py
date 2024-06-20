from fastapi import FastAPI

from src.to_do.router import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def read_root():
    return {"hello": "world"}
