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
    page_title="AI Marketing Agency",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 AI Marketing Agency")

st.write(
    "Multi-agent system that automatically generates marketing campaigns."
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
    "Product or service",
    placeholder="Ex: gaming keyboard"
)


# -----------------------------
# Gerar campanha
# -----------------------------
if st.button("Generate campaign"):

    if not produto:
        st.warning("Enter a product.")
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

    logs = []

    resultado_final = {}

    with st.spinner("🤖 AI agents working..."):

        with st.expander("Agent logs", expanded=False):

            log_container = st.empty()

            for passo in grafo.stream(estado_inicial):

                node = list(passo.keys())[0]
                dados = passo[node]

                if node == "pesquisa":
                    logs.append("🔎 Research agent analyzing market...")

                elif node == "estrategia":
                    logs.append("📊 Strategy agent creating campaign strategy...")

                elif node == "copywriter":
                    logs.append("✍️ Copywriter generating content...")

                elif node == "diretor_criativo":
                    logs.append("🎨 Creative director reviewing campaign...")

                elif node == "social":
                    logs.append("📱 Social media agent optimizing content...")

                log_container.markdown("\n".join(logs))

                resultado_final.update(dados)

    st.session_state.resultado = resultado_final


# -----------------------------
# Mostrar resultado
# -----------------------------
if st.session_state.resultado:

    resultado = st.session_state.resultado

    st.success("Campaign generated successfully")

    st.metric(
        "Tokens used",
        resultado.get("tokens_usados", 0)
    )

    st.divider()

    # -----------------------------
    # Tabs (mobile friendly)
    # -----------------------------
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Research",
        "Strategy",
        "Copy",
        "Creative Review",
        "Social Media"
    ])

    with tab1:
        st.markdown(resultado.get("pesquisa", {}).get("conteudo", ""))

    with tab2:
        st.markdown(resultado.get("estrategia", {}).get("conteudo", ""))

    with tab3:
        st.markdown(resultado.get("copy", {}).get("conteudo", ""))

    with tab4:
        st.markdown(resultado.get("revisao", {}).get("conteudo", ""))

    with tab5:
        conteudo_final = resultado.get("social", {}).get("conteudo", "")
        st.markdown(conteudo_final)

    st.divider()

    # -----------------------------
    # Preparar exportação
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

    pdf = None

    if conteudo_final:
        pdf = gerar_pdf(conteudo_final)

    # -----------------------------
    # Botões exportação
    # -----------------------------
    st.subheader("Export campaign")

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "⬇️ Download JSON",
            data=json_data,
            file_name="marketing_campaign.json",
            mime="application/json"
        )

    with col2:
        if pdf:
            st.download_button(
                "📄 Download PDF",
                data=pdf,
                file_name="marketing_campaign.pdf",
                mime="application/pdf"
            )

    st.divider()

    # -----------------------------
    # Copiar conteúdo
    # -----------------------------
    st.subheader("Copy campaign content")

    st.text_area(
        "Campaign text",
        conteudo_final,
        height=250
    )
