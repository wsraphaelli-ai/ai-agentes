from typing import TypedDict
from langgraph.graph import StateGraph

from app.agents.supervisor import supervisor_node
from app.agents.tecnico import tecnico_node
from app.agents.executivo import executivo_node

class Estado(TypedDict):
    pergunta: str
    tipo: str
    resposta: str

builder = StateGraph(Estado)

builder.add_node("supervisor", supervisor_node)
builder.add_node("tecnico", tecnico_node)
builder.add_node("executivo", executivo_node)

builder.set_entry_point("supervisor")

def rota(state):
    if "tecnico" in state["tipo"]:
        return "tecnico"
    return "executivo"

builder.add_conditional_edges(
    "supervisor",
    rota,
    {
        "tecnico": "tecnico",
        "executivo": "executivo"
    }
)

builder.set_finish_point("tecnico")
builder.set_finish_point("executivo")

graph = builder.compile()
