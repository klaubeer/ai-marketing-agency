from orquestrador.config_llm import llm


def diretor_criativo(estado):

    print("\n🎨 [Diretor Criativo] Revisando campanha...")

    conteudo = estado["copy"]["conteudo"]

    prompt = f"""
Você é Diretor Criativo de uma agência de publicidade.

Analise o conteúdo abaixo.

1) Dê uma nota de qualidade de 0 a 10
2) Melhore o conteúdo mantendo a estrutura

Conteúdo:
{conteudo}

Formato da resposta:

NOTA: X/10

VERSAO_APRIMORADA:
(conteúdo melhorado)
"""

    resposta = llm.invoke(prompt)

    texto = resposta.content
    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    estado["tokens_usados"] += tokens

    estado["revisao"] = {
        "conteudo": texto
    }

    print(f"✅ Campanha revisada | tokens usados: {tokens}")

    return estado
