from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def agente_pesquisa(estado: EstadoCampanha):

    print("\n🔎 [Agente Pesquisa] Analisando mercado...")

    produto = estado["produto"]

    prompt = f"""
Você é um especialista em pesquisa de mercado.

Produto:
{produto}

Forneça uma análise estruturada contendo:

1. Insights de mercado
2. Principais concorrentes
3. Tendências do setor
4. Perfil do consumidor
5. Oportunidades de marketing

Seja claro e objetivo, não tão longo.
"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    estado["tokens_usados"] += tokens

    # formato padrão esperado pelo frontend
    estado["pesquisa"] = {
        "conteudo": resposta.content
    }

    print(f"✅ Pesquisa concluída | tokens usados: {tokens}")

    return estado
