from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def agente_social_media(estado: EstadoCampanha):

    print("\n📱 [Social Media] Otimizando conteúdo...")

    conteudo_base = estado.get("revisao", {}).get(
        "conteudo",
        estado.get("copy", {}).get("conteudo", "")
    )

    if not conteudo_base:
        conteudo_base = "Campanha de marketing para o produto informado."

    prompt = f"""
Você é especialista em social media marketing.

Base da campanha:
{conteudo_base}

Crie conteúdo otimizado para redes sociais.

Gere:

1. Hashtags
- máximo 5 hashtags

2. Ideias de posts para Instagram
- até 5 ideias
- inclua uma breve descrição

3. Hooks para Reels
- até 5 frases curtas
- foco em engajamento
"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    print(f"✅ Conteúdo otimizado | tokens usados: {tokens}")

    return {
        "social": {"conteudo": resposta.content},
        "tokens_usados": estado["tokens_usados"] + tokens,
    }
