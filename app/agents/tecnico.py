from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-5.4")

def tecnico_node(state):
    pergunta = state["pergunta"]

    resposta = llm.invoke(f"Responda tecnicamente: {pergunta}")

    return {"resposta": resposta.content}
