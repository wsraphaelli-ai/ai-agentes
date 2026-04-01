from langchain_openai import ChatOpenAI
from app.utils import safe_response

llm = ChatOpenAI(model="gpt-4o-mini")

def executivo_node(state):
    pergunta = state["pergunta"]

    resp = llm.invoke(
        f"Responda de forma estratégica: {pergunta}"
    )

    return {"resposta": safe_response(resp)}
