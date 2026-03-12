from orquestrador.config_llm import llm


def diretor_criativo(estado):

    print("\n🎨 [Diretor Criativo] Revisando campanha...")

    conteudo = estado["copy"]["conteudo"]

    prompt = f"""
Você é Diretor Criativo de uma agência.

Revise e MELHORE o conteúdo abaixo.

REGRAS IMPORTANTES:

- NÃO resuma
- NÃO reduza seções
- NÃO corte ideias
- apenas melhore linguagem, impacto e criatividade

Se possível EXPANDA o conteúdo com mais exemplos ou detalhes.

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
