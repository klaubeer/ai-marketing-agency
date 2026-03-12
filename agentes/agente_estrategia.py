from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def agente_estrategia(estado: EstadoCampanha):

    print("\n📊 [Agente Estratégia] Criando estratégia...")

    produto = estado["produto"]

    pesquisa = estado.get("pesquisa", {}).get("conteudo", "")

    prompt = f"""
Você é um estrategista de marketing.

Produto:
{produto}

Pesquisa de mercado:
{pesquisa}

Crie uma estratégia contendo:

1. Público-alvo
2. Posicionamento da marca
3. Ângulo da campanha
4. Canais de marketing recomendados

Seja claro e objetivo.
"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    estado["tokens_usados"] += tokens

    estado["estrategia"] = {
        "conteudo": resposta.content
    }

    print(f"✅ Estratégia definida | tokens usados: {tokens}")

    return estado
