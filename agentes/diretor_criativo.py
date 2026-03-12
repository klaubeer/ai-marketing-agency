from orquestrador.config_llm import llm


def diretor_criativo(estado):

    print("\n🎨 [Diretor Criativo] Revisando campanha...")

    conteudo = estado["conteudo"]

    prompt = f"""
Você é um Diretor Criativo de uma grande agência de publicidade.

Sua tarefa é revisar e melhorar o conteúdo de marketing criado por um copywriter.

Analise:

- Clareza da mensagem
- Força persuasiva
- Criatividade
- Adequação ao público
- Impacto de marketing

Se necessário, reescreva e melhore o conteúdo.

Conteúdo da campanha:
{conteudo}

Retorne a versão aprimorada da campanha.
"""

    resposta = llm.invoke(prompt)

    conteudo_revisado = resposta.content

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    print(f"✅ Campanha aprimorada | tokens usados: {tokens}")

    estado["conteudo"] = conteudo_revisado
    estado["tokens_totais"] += tokens

    return estado
