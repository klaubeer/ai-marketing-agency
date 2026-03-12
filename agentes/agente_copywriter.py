from langchain_openai import ChatOpenAI
from orquestrador.estado_campanha import EstadoCampanha

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


def agente_copywriter(estado: EstadoCampanha):

    print("\n✍️ [Copywriter] Criando conteúdo da campanha...")

    estrategia = estado["estrategia"]["plano"]

    prompt = f"""
Você é um copywriter profissional de marketing.

Com base na seguinte estratégia de campanha:

{estrategia}

Crie:

1. 3 ideias de posts
2. Legendas para redes sociais
3. Texto de anúncio (ad copy)

Seja criativo e persuasivo, mas responda de forma objetiva.

Limites:
- máximo 5 tópicos por seção
- frases curtas
- evite textos longos
"""

    resposta = llm.invoke(prompt)

    estado["copy"] = {
        "conteudo": resposta.content
    }

    print("✅ [Copywriter] Conteúdo criado")

    return estado
