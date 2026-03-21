from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def agente_copywriter(estado: EstadoCampanha):

    tentativas = estado.get("tentativas_revisao", 0)

    if tentativas > 0:
        nota = estado.get("nota_revisao", 0)
        feedback = estado.get("revisao", {}).get("conteudo", "")
        print(f"\n✍️ [Copywriter] Revisando conteúdo (tentativa {tentativas + 1}, nota anterior: {nota}/10)...")
    else:
        print("\n✍️ [Copywriter] Gerando conteúdo...")

    estrategia = estado.get("estrategia", {}).get("conteudo", "")

    if tentativas > 0:
        prompt = f"""
Você é um copywriter profissional especializado em marketing digital.

Estratégia da campanha:
{estrategia}

O Diretor Criativo revisou sua versão anterior e deu nota {nota}/10.
Feedback e versão anterior para referência:
{feedback}

Reescreva o conteúdo de marketing incorporando as melhorias sugeridas.
Seja mais criativo, impactante e persuasivo desta vez.

Entregue:

1. Ideias de posts
- pelo menos 3 ideias

2. Legendas para redes sociais
- pelo menos 3 legendas completas

3. Textos de anúncio
- pelo menos 2 ad copies
"""
    else:
        prompt = f"""
Você é um copywriter profissional especializado em marketing digital.

Estratégia da campanha:
{estrategia}

Crie conteúdo de marketing contendo:

1. Ideias de posts
- pelo menos 3 ideias

2. Legendas para redes sociais
- pelo menos 3 legendas completas

3. Textos de anúncio
- pelo menos 2 ad copies

Seja criativo e persuasivo, mas não muito longo.
"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    print(f"✅ Conteúdo criado | tokens usados: {tokens}")

    return {
        "copy": {"conteudo": resposta.content},
        "tokens_usados": estado["tokens_usados"] + tokens,
    }
