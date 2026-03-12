from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def agente_social_media(estado: EstadoCampanha):

    print("\n📱 [Social Media] Otimizando conteúdo...")

    copy = estado["copy"]["conteudo"]

    prompt = f"""
Você é especialista em social media.

Conteúdo:
{copy}

Gere:

1. hashtags
2. ideias de posts instagram
3. hooks para reels

Limites:
- máximo 5 hashtags

"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    estado["tokens_usados"] += tokens

    estado["social"] = {
        "conteudo": resposta.content
    }

    print(f"✅ Conteúdo otimizado | tokens usados: {tokens}")

    return estado
