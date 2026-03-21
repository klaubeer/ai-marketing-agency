import re

from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm


def diretor_criativo(estado: EstadoCampanha):

    tentativas = estado.get("tentativas_revisao", 0)
    print(f"\n🎨 [Diretor Criativo] Revisando campanha (revisão {tentativas + 1})...")

    conteudo = estado["copy"]["conteudo"]

    prompt = f"""
Você é Diretor Criativo de uma agência de marketing.

Revise e MELHORE o conteúdo abaixo.

REGRAS IMPORTANTES:

- NÃO resuma
- NÃO reduza seções
- NÃO corte ideias
- apenas melhore linguagem, impacto e criatividade

Se possível EXPANDA o conteúdo com mais exemplos ou detalhes.

Conteúdo:
{conteudo}

Formato da resposta (siga exatamente):

NOTA: X/10

VERSAO_APRIMORADA:
(conteúdo melhorado aqui)
"""

    resposta = llm.invoke(prompt)

    texto = resposta.content
    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    # extrai a nota numérica do texto
    match = re.search(r"NOTA:\s*(\d+(?:\.\d+)?)/10", texto)
    nota = int(float(match.group(1))) if match else 7

    print(f"✅ Campanha revisada | nota: {nota}/10 | tokens usados: {tokens}")

    return {
        "revisao": {"conteudo": texto},
        "nota_revisao": nota,
        "tentativas_revisao": tentativas + 1,
        "tokens_usados": estado["tokens_usados"] + tokens,
    }
