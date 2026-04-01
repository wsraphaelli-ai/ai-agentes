from fastapi import FastAPI
from pydantic import BaseModel

from app.graph import graph

# 👉 CRIA O APP (isso estava faltando)
app = FastAPI(title="AI Agentes API")

# 👉 Modelo de entrada
class Pergunta(BaseModel):
    pergunta: str

# 👉 Rota inicial
@app.get("/")
def home():
    return {"status": "ok"}

# 👉 Rota principal
@app.post("/chat")
def chat(req: Pergunta):
    try:
        resultado = graph.invoke({"pergunta": req.pergunta})
        return resultado
    except Exception as e:
        return {"erro": str(e)}
