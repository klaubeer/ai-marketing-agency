from langchain_openai import ChatOpenAI
from orquestrador.estado_campanha import EstadoCampanha

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7
)


def agente_estrategia(estado: EstadoCampanha):

    produto = estado["produto"]
    pesquisa = estado["pesquisa"]["analise"]

    prompt = f"""
Você é um estrategista de marketing.

Produto:
{produto}

Pesquisa de mercado:
{pesquisa}

Crie:

1. Público alvo
2. Posicionamento da campanha
3. Ângulo da campanha
4. Canais de marketing recomendados
"""

    resposta = llm.invoke(prompt)

    estado["estrategia"] = {
        "plano": resposta.content
    }

    return estado
