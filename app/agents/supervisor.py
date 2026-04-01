from langchain_openai import ChatOpenAI
from app.utils import safe_response

llm = ChatOpenAI(model="gpt-4o-mini")

def supervisor_node(state):
    pergunta = state["pergunta"]

    resp = llm.invoke(
        f"Classifique como 'tecnico' ou 'executivo': {pergunta}"
    )

    tipo = safe_response(resp).lower()

    return {"tipo": tipo}
