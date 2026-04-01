from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import graph

app = FastAPI()

class Pergunta(BaseModel):
    pergunta: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: Pergunta):
    return graph.invoke({"pergunta": req.pergunta})
