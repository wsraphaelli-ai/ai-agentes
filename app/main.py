@app.post("/chat")
def chat(req: Pergunta):
    try:
        resultado = graph.invoke({"pergunta": req.pergunta})
        return resultado
    except Exception as e:
        return {"erro": str(e)}
