from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

def supervisor_node(state):
    pergunta = state["pergunta"]

    resposta = llm.invoke(
        f"Classifique como 'tecnico' ou 'executivo': {pergunta}"
    )

    return {"tipo": resposta.content.strip().lower()}
