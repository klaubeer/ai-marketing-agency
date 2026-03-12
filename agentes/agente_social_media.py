from langchain_openai import ChatOpenAI
from orquestrador.estado_campanha import EstadoCampanha

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


def agente_social_media(estado: EstadoCampanha):

    copy = estado["copy"]["conteudo"]

    prompt = f"""
Você é um especialista em social media.

Conteúdo gerado:

{copy}

Otimize para redes sociais e gere:

1. Hashtags
2. Sugestões de posts para Instagram
3. Hooks para TikTok
"""

    resposta = llm.invoke(prompt)

    estado["social"] = {
        "conteudo": resposta.content
    }

    return estado
