from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm
from orquestrador.config_sentinela import get_handler


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

Seja claro e objetivo, não muito longo.
"""

    resposta = llm.invoke(prompt, config={"callbacks": [get_handler("estrategia")]})

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    print(f"✅ Estratégia definida | tokens usados: {tokens}")

    return {
        "estrategia": {"conteudo": resposta.content},
        "tokens_usados": estado["tokens_usados"] + tokens,
    }
