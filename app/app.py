import sys
import os
import json
import io

# permite importar módulos da raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from orquestrador.grafo_agentes import construir_grafo

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


# -----------------------------
# Função para gerar PDF
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

produto = st.text_input(
    "Digite o produto ou serviço",
    placeholder="Ex: teclado gamer"
)

# -----------------------------
# Botão gerar campanha
# -----------------------------
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

    st.subheader("⚙️ Execução dos agentes")

    log_container = st.empty()

    logs = []

    resultado_final = None

    # execução em streaming do LangGraph
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

    # -----------------------------
    # Seções da campanha
    # -----------------------------

    st.header("🧠 Pesquisa de Mercado")
    if resultado_final.get("pesquisa"):
        st.markdown(resultado_final["pesquisa"].get("conteudo", ""))

    st.divider()

    st.header("📊 Estratégia da Campanha")
    if resultado_final.get("estrategia"):
        st.markdown(resultado_final["estrategia"].get("conteudo", ""))

    st.divider()

    st.header("✍️ Conteúdo Criado")
    if resultado_final.get("copy"):
        st.markdown(resultado_final["copy"].get("conteudo", ""))

    st.divider()

    st.header("🎨 Revisão do Diretor Criativo")
    if resultado_final.get("revisao"):
        st.markdown(resultado_final["revisao"].get("conteudo", ""))

    st.divider()

    st.header("📱 Conteúdo Final para Redes Sociais")

    conteudo_final = ""

    if resultado_final.get("social"):
        conteudo_final = resultado_final["social"].get("conteudo", "")
        st.markdown(conteudo_final)

    st.divider()

    # -----------------------------
    # Tokens
    # -----------------------------
    st.metric(
        label="Tokens utilizados",
        value=resultado_final["tokens_usados"]
    )

    st.divider()

    # -----------------------------
    # Exportar JSON
    # -----------------------------
    campanha = {
        "produto": produto,
        "pesquisa": resultado_final.get("pesquisa"),
        "estrategia": resultado_final.get("estrategia"),
        "copy": resultado_final.get("copy"),
        "revisao": resultado_final.get("revisao"),
        "social": resultado_final.get("social"),
        "tokens_usados": resultado_final["tokens_usados"]
    }

    json_data = json.dumps(campanha, indent=2, ensure_ascii=False)

    st.download_button(
        label="⬇️ Baixar campanha em JSON",
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
            label="📄 Baixar campanha em PDF",
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
