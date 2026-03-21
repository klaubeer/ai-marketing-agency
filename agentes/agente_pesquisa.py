from orquestrador.estado_campanha import EstadoCampanha
from orquestrador.config_llm import llm
from ferramentas.busca_web import buscar_na_web


def agente_pesquisa(estado: EstadoCampanha):

    print("\n🔎 [Agente Pesquisa] Analisando mercado...")

    produto = estado["produto"]

    print("   🌐 Buscando dados atuais na web...")
    dados_web = buscar_na_web(f"{produto} mercado tendências concorrentes")

    prompt = f"""
Você é um especialista em pesquisa de mercado.

Produto:
{produto}

Dados recentes da web:
{dados_web}

Com base nos dados acima, forneça uma análise estruturada contendo:

1. Insights de mercado
2. Principais concorrentes
3. Tendências do setor
4. Perfil do consumidor
5. Oportunidades de marketing

Seja claro e objetivo, não tão longo.
"""

    resposta = llm.invoke(prompt)

    tokens = resposta.response_metadata["token_usage"]["total_tokens"]

    print(f"✅ Pesquisa concluída | tokens usados: {tokens}")

    return {
        "pesquisa": {"conteudo": resposta.content},
        "tokens_usados": estado["tokens_usados"] + tokens,
    }
