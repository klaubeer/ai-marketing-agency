from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def agente_copywriter(estado: EstadoCampanha):

    print("\n✍️ [Copywriter] Gerando conteúdo...")

    estrategia = estado["estrategia"]["plano"]

    prompt = f"""
Você é um copywriter profissional.

Estratégia:
{estrategia}

Crie:

1. 3 ideias de posts
2. legendas
3. ad copy 

Gere pelo menos:

3 ideias de posts
3 legendas completas
2 textos de anúncio
"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    estado["tokens_usados"] += tokens

    estado["copy"] = {
        "conteudo": resposta.content
    }

    print(f"✅ Conteúdo criado | tokens usados: {tokens}")

    return estado
