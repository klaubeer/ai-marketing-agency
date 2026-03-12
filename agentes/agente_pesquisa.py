
from langchain_openai import ChatOpenAI
from orquestrador.estado_campanha import EstadoCampanha

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7
)


def agente_pesquisa(estado: EstadoCampanha):

    produto = estado["produto"]

    prompt = f"""
Você é um especialista em pesquisa de mercado.

Analise o mercado para o seguinte produto:

{produto}

Forneça:

1. Insights de mercado
2. Principais concorrentes
3. Tendências do setor
"""

    resposta = llm.invoke(prompt)

    estado["pesquisa"] = {
        "analise": resposta.content
    }

    return estado
