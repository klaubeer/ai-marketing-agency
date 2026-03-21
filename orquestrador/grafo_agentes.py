from langgraph.graph import StateGraph, END

from orquestrador.estado_campanha import EstadoCampanha

from agentes.agente_pesquisa import agente_pesquisa
from agentes.agente_estrategia import agente_estrategia
from agentes.agente_copywriter import agente_copywriter
from agentes.agente_social_media import agente_social_media
from agentes.diretor_criativo import diretor_criativo


def roteador_revisao(estado: EstadoCampanha) -> str:
    """
    Após o Diretor Criativo, decide se o conteúdo já está bom o suficiente
    (nota >= 7) ou se precisa de mais uma rodada com o Copywriter.
    Limite de 2 tentativas para evitar loops infinitos.
    """
    nota = estado.get("nota_revisao", 0)
    tentativas = estado.get("tentativas_revisao", 0)

    if nota >= 7 or tentativas >= 2:
        return "social"

    return "copywriter"


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

    # edge condicional: diretor aprova (nota >= 7) → social
    #                   diretor reprova (nota < 7)  → copywriter (até 2x)
    fluxo.add_conditional_edges(
        "diretor_criativo",
        roteador_revisao,
        {
            "copywriter": "copywriter",
            "social": "social",
        },
    )

    fluxo.add_edge("social", END)

    grafo = fluxo.compile()

    return grafo
