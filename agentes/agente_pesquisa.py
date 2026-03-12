from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def agente_pesquisa(estado: EstadoCampanha):

    print("\n🔎 [Agente Pesquisa] Analisando mercado...")

    produto = estado["produto"]

    prompt = f"""
Você é especialista em pesquisa de mercado.

Produto:
{produto}

Forneça:

1. insights de mercado
2. concorrentes
3. tendências

Limites:
- máximo 5 tópicos
- frases curtas
"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    estado["tokens_usados"] += tokens

    estado["pesquisa"] = {
        "analise": resposta.content
    }

    print(f"✅ Pesquisa concluída | tokens usados: {tokens}")

    return estado
