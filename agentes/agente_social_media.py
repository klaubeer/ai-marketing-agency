from langchain_openai import ChatOpenAI
from orquestrador.estado_campanha import EstadoCampanha

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


def agente_social_media(estado: EstadoCampanha):

    print("\n📱 [Social Media] Adaptando conteúdo para redes sociais...")

    copy = estado["copy"]["conteudo"]

    prompt = f"""
Você é um especialista em social media.

Com base no conteúdo abaixo:

{copy}

Gere:

1. Hashtags relevantes
2. Sugestões de posts para Instagram
3. Hooks curtos para TikTok ou Reels

Foque em engajamento.
"""

    resposta = llm.invoke(prompt)

    estado["social"] = {
        "conteudo": resposta.content
    }

    print("✅ [Social Media] Conteúdo otimizado para redes sociais")

    return estado
