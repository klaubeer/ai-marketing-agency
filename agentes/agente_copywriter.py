from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def agente_copywriter(estado: EstadoCampanha):

    print("\n✍️ [Copywriter] Gerando conteúdo...")

    estrategia = estado.get("estrategia", {}).get("conteudo", "")

    prompt = f"""
Você é um copywriter profissional especializado em marketing digital.

Estratégia da campanha:
{estrategia}

Crie conteúdo de marketing contendo:

1. Ideias de posts
- pelo menos 3 ideias

2. Legendas para redes sociais
- pelo menos 3 legendas completas

3. Textos de anúncio
- pelo menos 2 ad copies

Seja criativo e persuasivo.
"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    estado["tokens_usados"] += tokens

    estado["copy"] = {
        "conteudo": resposta.content
    }

    print(f"✅ Conteúdo criado | tokens usados: {tokens}")

    return estado
