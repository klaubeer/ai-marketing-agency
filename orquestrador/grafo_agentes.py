from langgraph.graph import StateGraph
from orquestrador.estado_campanha import EstadoCampanha

from agentes.agente_pesquisa import agente_pesquisa
from agentes.agente_estrategia import agente_estrategia
from agentes.agente_copywriter import agente_copywriter
from agentes.agente_social_media import agente_social_media
from agentes.diretor_criativo import diretor_criativo


def construir_grafo():

    fluxo = StateGraph(EstadoCampanha)

    fluxo.add_node("pesquisa", agente_pesquisa)
    fluxo.add_node("estrategia", agente_estrategia)
    fluxo.add_node("copywriter", agente_copywriter)
    fluxo.add_node("diretor_criativo", diretor_criativo)
    fluxo.add_node("social", agente_social_media)

    fluxo.set_entry_point("pesquisa")

    fluxo.add_edge("pesquisa", "estrategia")
    fluxo.add_edge("estrategia", "copywriter")
    fluxo.add_edge("copywriter", "diretor_criativo")
    fluxo.add_edge("diretor_criativo", "social")

    grafo = fluxo.compile()

    return grafo
