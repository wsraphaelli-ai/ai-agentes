from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def tecnico_node(state):
    pergunta = state["pergunta"]

    resposta = llm.invoke(
        f"Responda tecnicamente com precisão: {pergunta}"
    )

    return {"resposta": resposta.content}
