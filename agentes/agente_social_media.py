from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def agente_social_media(estado: EstadoCampanha):

    print("\n📱 [Social Media] Otimizando conteúdo...")

    # usa revisão do diretor criativo se existir
    conteudo_base = estado.get("revisao", {}).get(
        "conteudo",
        estado.get("copy", {}).get("conteudo", "")
    )

    prompt = f"""
Você é especialista em social media.

Conteúdo da campanha:
{conteudo_base}

Crie conteúdo otimizado para redes sociais.

Gere:

### Hashtags
- máximo 5 hashtags
- relevantes para marketing digital

### Ideias de posts para Instagram
- até 5 ideias
- inclua descrição curta

### Hooks para Reels
- até 5 frases curtas
- foco em engajamento
"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    estado["tokens_usados"] += tokens

    estado["social"] = {
        "conteudo": resposta.content
    }

    print(f"✅ Conteúdo otimizado | tokens usados: {tokens}")

    return estado
