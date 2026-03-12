from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def agente_estrategia(estado: EstadoCampanha):

    print("\n📊 [Agente Estratégia] Criando estratégia...")

    produto = estado["produto"]
    pesquisa = estado["pesquisa"]["analise"]

    prompt = f"""
Você é estrategista de marketing.

Produto:
{produto}

Pesquisa:
{pesquisa}

Crie:

1. público alvo
2. posicionamento
3. ângulo da campanha
4. canais de marketing

Limites:
- máximo 4 tópicos
- respostas objetivas
"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    estado["tokens_usados"] += tokens

    estado["estrategia"] = {
        "plano": resposta.content
    }

    print(f"✅ Estratégia definida | tokens usados: {tokens}")

    return estado
