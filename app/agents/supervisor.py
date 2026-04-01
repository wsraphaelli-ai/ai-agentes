from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-5.4", temperature=0)

def supervisor_node(state):
    pergunta = state["pergunta"]

    prompt = f"""
    Classifique a pergunta como:
    - tecnico
    - executivo

    Pergunta: {pergunta}
    """

    tipo = llm.invoke(prompt).content.lower()

    return {"tipo": tipo}
