import sys
import os
import time

# permite importar módulos da raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from orquestrador.grafo_agentes import construir_grafo


st.set_page_config(
    page_title="Agência de Marketing IA",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Agência de Marketing com IA")
st.write(
    "Sistema multi-agente que gera campanhas de marketing automaticamente."
)

st.divider()

produto = st.text_input(
    "Digite o produto ou serviço",
    placeholder="Ex: teclado gamer"
)

if st.button("Gerar campanha"):

    if not produto:
        st.warning("Digite um produto primeiro.")
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

    status = st.empty()

    # simula execução dos agentes
    status.write("🔎 **Agente Pesquisa** analisando mercado...")
    time.sleep(1)

    status.write("📊 **Agente Estratégia** criando estratégia...")
    time.sleep(1)

    status.write("✍️ **Copywriter** gerando conteúdo...")
    time.sleep(1)

    status.write("🎨 **Diretor Criativo** revisando campanha...")
    time.sleep(1)

    status.write("📱 **Social Media** otimizando conteúdo...")
    time.sleep(1)

    with st.spinner("Executando agentes..."):

        resultado = grafo.invoke(estado_inicial)

    status.success("✅ Campanha gerada com sucesso!")

    st.divider()

    st.header("🧠 Pesquisa de Mercado")

    if resultado.get("pesquisa"):
        st.markdown(resultado["pesquisa"].get("conteudo", ""))

    st.divider()

    st.header("📊 Estratégia da Campanha")

    if resultado.get("estrategia"):
        st.markdown(resultado["estrategia"].get("conteudo", ""))

    st.divider()

    st.header("✍️ Conteúdo Criado")

    if resultado.get("copy"):
        st.markdown(resultado["copy"].get("conteudo", ""))

    st.divider()

    st.header("🎨 Revisão do Diretor Criativo")

    if resultado.get("revisao"):
        st.markdown(resultado["revisao"].get("conteudo", ""))

    st.divider()

    st.header("📱 Conteúdo Final para Redes Sociais")

    if resultado.get("social"):
        st.markdown(resultado["social"].get("conteudo", ""))

    st.divider()

    st.metric(
        label="Tokens utilizados",
        value=resultado["tokens_usados"]
    )
