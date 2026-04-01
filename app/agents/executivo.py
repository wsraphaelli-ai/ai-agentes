from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-5.4")

def executivo_node(state):
    pergunta = state["pergunta"]

    resposta = llm.invoke(f"Responda de forma executiva: {pergunta}")

    return {"resposta": resposta.content}
