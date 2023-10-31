from fastapi import FastAPI

from app.api import handle_get_link, handle_create_link

app = FastAPI()


@app.post("/create")
async def create_link(url: str):
    return handle_create_link(url)


@app.get("/link/{key}")
async def get_link(key: str):
    return handle_get_link(key)
