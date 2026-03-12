from langchain_openai import ChatOpenAI
from orquestrador.estado_campanha import EstadoCampanha

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


def agente_pesquisa(estado: EstadoCampanha):

    print("\n🔎 [Agente Pesquisa] Iniciando análise de mercado...")

    produto = estado["produto"]

    prompt = f"""
Você é um especialista em pesquisa de mercado.

Analise o mercado para o seguinte produto:

{produto}

Forneça:

1. Insights de mercado
2. Principais concorrentes
3. Tendências do setor

Responda de forma estruturada e clara.
Limites:
- máximo 5 tópicos por seção
- frases curtas
- evite textos longos
"""

    resposta = llm.invoke(prompt)

    estado["pesquisa"] = {
        "analise": resposta.content
    }

    print("✅ [Agente Pesquisa] Pesquisa concluída")

    return estado
