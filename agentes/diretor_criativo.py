from orquestrador.config_llm import llm


def diretor_criativo(estado):

    print("\n🎨 [Diretor Criativo] Revisando campanha...")

    conteudo = estado["copy"]["conteudo"]

    prompt = f"""
Você é um Diretor Criativo de uma grande agência de publicidade.

Revise e melhore o conteúdo de marketing abaixo.

Analise:
- clareza
- criatividade
- impacto
- persuasão

Melhore o conteúdo mantendo a estrutura.

Conteúdo:
{conteudo}
"""

    resposta = llm.invoke(prompt)

    conteudo_revisado = resposta.content

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    print(f"✅ Campanha aprimorada | tokens usados: {tokens}")

    estado["revisao"] = {
        "conteudo": conteudo_revisado
    }

    estado["tokens_usados"] += tokens

    return estado
