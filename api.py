from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def hello_world():
    return "bonjour les gens"

@app.get("/article/{id}")
async def get_component(id:int):
    return {"article_id": id}


class Coord(BaseModel):
    firstname : string
    lastname : string

@app.post("/create")
async def create_personne(coord:Coord):
    return {"je suis un personnage"}

if __name__ == "__main__":
    uvicorn.run(app, host= "127.0.0.1", port=8000)