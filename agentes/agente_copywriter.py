
from langchain_openai import ChatOpenAI
from orquestrador.estado_campanha import EstadoCampanha

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


def agente_copywriter(estado: EstadoCampanha):

    estrategia = estado["estrategia"]["plano"]

    prompt = f"""
Você é um copywriter profissional.

Estratégia da campanha:

{estrategia}

Crie:

1. 3 ideias de posts
2. Legendas
3. Texto de anúncio (ad copy)
"""

    resposta = llm.invoke(prompt)

    estado["copy"] = {
        "conteudo": resposta.content
    }

    return estado
