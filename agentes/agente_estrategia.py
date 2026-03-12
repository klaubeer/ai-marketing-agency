from langchain_openai import ChatOpenAI
from orquestrador.estado_campanha import EstadoCampanha

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


def agente_estrategia(estado: EstadoCampanha):

    print("\n📊 [Agente Estratégia] Desenvolvendo estratégia da campanha...")

    produto = estado["produto"]
    pesquisa = estado["pesquisa"]["analise"]

    prompt = f"""
Você é um estrategista de marketing.

Produto:
{produto}

Pesquisa de mercado:
{pesquisa}

Crie uma estratégia de campanha contendo:

1. Público-alvo
2. Posicionamento da marca
3. Ângulo da campanha
4. Canais de marketing recomendados

Explique de forma clara e objetiva.

Limites:
- máximo 5 tópicos por seção
- frases curtas
- evite textos longos
"""

    resposta = llm.invoke(prompt)

    estado["estrategia"] = {
        "plano": resposta.content
    }

    print("✅ [Agente Estratégia] Estratégia definida")

    return estado
