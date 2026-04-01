from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def executivo_node(state):
    pergunta = state["pergunta"]

    resposta = llm.invoke(
        f"Responda de forma estratégica: {pergunta}"
    )

    return {"resposta": resposta.content}
