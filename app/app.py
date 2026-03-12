import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from orquestrador.grafo_agentes import construir_grafo


st.set_page_config(
    page_title="Agência de Marketing IA",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Agência de Marketing com IA")
st.write("Sistema multi-agente que gera campanhas automaticamente.")

st.divider()

produto = st.text_input(
    "Digite o produto ou serviço",
    placeholder="Ex: teclado gamer"
)

if st.button("Gerar campanha"):

    if not produto:
        st.warning("Digite um produto.")
        st.stop()

    estado_inicial = {
        "produto": produto,
        "pesquisa": {},
        "estrategia": {},
        "copy": {},
        "revisao": {},
        "social": {},
        "tokens_usados": 0
    }

    grafo = construir_grafo()

    st.subheader("⚙️ Execução dos agentes")

    log_container = st.empty()

    logs = []

    resultado_final = None

    for passo in grafo.stream(estado_inicial):

        node = list(passo.keys())[0]

        if node == "pesquisa":
            logs.append("🔎 **Agente Pesquisa** analisando mercado...")

        elif node == "estrategia":
            logs.append("📊 **Agente Estratégia** criando estratégia...")

        elif node == "copywriter":
            logs.append("✍️ **Copywriter** gerando conteúdo...")

        elif node == "diretor_criativo":
            logs.append("🎨 **Diretor Criativo** revisando campanha...")

        elif node == "social":
            logs.append("📱 **Social Media** otimizando conteúdo...")

        log_container.markdown("\n".join(logs))

        resultado_final = passo[node]

    st.success("✅ Campanha gerada")

    st.divider()

    st.header("📱 Conteúdo Final")

    st.markdown(resultado_final["social"]["conteudo"])

    st.metric(
        "Tokens utilizados",
        resultado_final["tokens_usados"]
    )
