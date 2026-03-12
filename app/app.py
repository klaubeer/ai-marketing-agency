import sys
import os
import json
import io

# permite importar módulos da raiz do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from orquestrador.grafo_agentes import construir_grafo

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


# -----------------------------
# Gerar PDF
# -----------------------------
def gerar_pdf(texto):

    buffer = io.BytesIO()

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(buffer)

    elementos = []

    for linha in texto.split("\n"):
        elementos.append(Paragraph(linha, styles["Normal"]))
        elementos.append(Spacer(1, 6))

    doc.build(elementos)

    buffer.seek(0)

    return buffer


# -----------------------------
# Configuração da página
# -----------------------------
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


# -----------------------------
# Session State
# -----------------------------
if "resultado" not in st.session_state:
    st.session_state.resultado = None

if "produto" not in st.session_state:
    st.session_state.produto = ""


# -----------------------------
# Input do usuário
# -----------------------------
produto = st.text_input(
    "Digite o produto ou serviço",
    placeholder="Ex: teclado gamer"
)


# -----------------------------
# Gerar campanha
# -----------------------------
if st.button("Gerar campanha"):

    if not produto:
        st.warning("Digite um produto.")
        st.stop()

    st.session_state.produto = produto

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

    log_container = st.empty()

    logs = []

    resultado_final = {}

    with st.spinner("🤖 Agentes trabalhando..."):

        for passo in grafo.stream(estado_inicial):

            node = list(passo.keys())[0]
            dados = passo[node]

            if node == "pesquisa":
                logs.append("🔎 Agente Pesquisa analisando mercado...")

            elif node == "estrategia":
                logs.append("📊 Agente Estratégia criando estratégia...")

            elif node == "copywriter":
                logs.append("✍️ Copywriter gerando conteúdo...")

            elif node == "diretor_criativo":
                logs.append("🎨 Diretor Criativo revisando campanha...")

            elif node == "social":
                logs.append("📱 Social Media otimizando conteúdo...")

            log_container.markdown("\n".join(logs))

            # acumula o estado completo
            resultado_final.update(dados)

    st.session_state.resultado = resultado_final


# -----------------------------
# Mostrar resultado
# -----------------------------
if st.session_state.resultado:

    resultado = st.session_state.resultado

    st.success("✅ Campanha gerada")

    st.divider()

    st.header("🧠 Pesquisa de Mercado")
    st.markdown(resultado.get("pesquisa", {}).get("conteudo", ""))

    st.divider()

    st.header("📊 Estratégia da Campanha")
    st.markdown(resultado.get("estrategia", {}).get("conteudo", ""))

    st.divider()

    st.header("✍️ Conteúdo Criado")
    st.markdown(resultado.get("copy", {}).get("conteudo", ""))

    st.divider()

    st.header("🎨 Revisão Criativa")
    st.markdown(resultado.get("revisao", {}).get("conteudo", ""))

    st.divider()

    st.header("📱 Conteúdo Final para Redes Sociais")

    conteudo_final = resultado.get("social", {}).get("conteudo", "")

    st.markdown(conteudo_final)

    st.divider()

    st.metric(
        "Tokens utilizados",
        resultado.get("tokens_usados", 0)
    )

    st.divider()

    # -----------------------------
    # Exportar JSON
    # -----------------------------
    campanha = {
        "produto": st.session_state.produto,
        "pesquisa": resultado.get("pesquisa"),
        "estrategia": resultado.get("estrategia"),
        "copy": resultado.get("copy"),
        "revisao": resultado.get("revisao"),
        "social": resultado.get("social"),
        "tokens_usados": resultado.get("tokens_usados", 0)
    }

    json_data = json.dumps(campanha, indent=2, ensure_ascii=False)

    st.download_button(
        "⬇️ Baixar campanha em JSON",
        data=json_data,
        file_name="campanha_marketing.json",
        mime="application/json"
    )

    # -----------------------------
    # Exportar PDF
    # -----------------------------
    if conteudo_final:

        pdf = gerar_pdf(conteudo_final)

        st.download_button(
            "📄 Baixar campanha em PDF",
            data=pdf,
            file_name="campanha_marketing.pdf",
            mime="application/pdf"
        )

    # -----------------------------
    # Copiar conteúdo
    # -----------------------------
    st.subheader("📋 Copiar conteúdo da campanha")

    st.text_area(
        "Copie o conteúdo abaixo",
        conteudo_final,
        height=300
    )
