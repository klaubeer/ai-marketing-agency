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
    page_title="Agência de Marketing com IA",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Agência de Marketing com IA")

st.write("Sistema multi-agente que gera sugestões de campanha de marketing automaticamente.")

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
with st.form("form_campanha"):
    produto = st.text_input(
        "Digite o produto ou serviço para qual deseja gerar uma campanha:",
        placeholder="Ex: teclado gamer"
    )
    submitted = st.form_submit_button("Gerar campanha")

# -----------------------------
# Gerar campanha
# -----------------------------
if submitted:

    if not produto:
        st.warning("Digite um produto ou serviço.")
        st.stop()

    st.session_state.produto = produto

    estado_inicial = {
        "produto": produto,
        "pesquisa": {},
        "estrategia": {},
        "copy": {},
        "revisao": {},
        "social": {},
        "nota_revisao": 0,
        "tentativas_revisao": 0,
        "tokens_usados": 0,
        "historico": {},
    }

    grafo = construir_grafo()

    logs = []
    resultado_final = {}

    with st.spinner("🤖 Agentes de IA trabalhando..."):

        with st.expander("Logs dos agentes", expanded=False):

            log_container = st.empty()

            for passo in grafo.stream(estado_inicial):

                node = list(passo.keys())[0]
                dados = passo[node]

                tentativas = dados.get("tentativas_revisao", resultado_final.get("tentativas_revisao", 0))
                nota = dados.get("nota_revisao", resultado_final.get("nota_revisao", 0))

                if node == "pesquisa":
                    logs.append("🔎 Agente de Pesquisa buscando dados na web e analisando o mercado...")

                elif node == "estrategia":
                    logs.append("📊 Agente de Estratégia definindo posicionamento da campanha...")

                elif node == "copywriter":
                    if tentativas > 0:
                        logs.append(f"✍️ Copywriter revisando conteúdo (tentativa {tentativas + 1}, nota anterior: {nota}/10)...")
                    else:
                        logs.append("✍️ Copywriter gerando conteúdo da campanha...")

                elif node == "diretor_criativo":
                    logs.append(f"🎨 Diretor Criativo revisando campanha (revisão {tentativas + 1})...")

                elif node == "social":
                    logs.append("📱 Agente de Social Media adaptando conteúdo para redes sociais...")

                log_container.markdown("\n\n".join(logs))

                resultado_final.update(dados)

    # log final com resultado da revisão
    nota_final = resultado_final.get("nota_revisao", 0)
    tentativas_final = resultado_final.get("tentativas_revisao", 0)
    logs.append(f"✅ Campanha finalizada | nota criativa: {nota_final}/10 | revisões: {tentativas_final}")
    log_container.markdown("\n".join(logs))

    st.session_state.resultado = resultado_final


# -----------------------------
# Mostrar resultado
# -----------------------------
if st.session_state.resultado:

    resultado = st.session_state.resultado

    st.success("✅ Sugestão de campanha gerada")

    col_tok, col_nota, col_rev = st.columns(3)

    with col_tok:
        st.metric("Tokens utilizados", resultado.get("tokens_usados", 0))

    with col_nota:
        st.metric("Nota criativa", f"{resultado.get('nota_revisao', 0)}/10")

    with col_rev:
        st.metric("Revisões feitas", resultado.get("tentativas_revisao", 0))

    st.divider()

    # -----------------------------
    # Abas
    # -----------------------------
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Pesquisa de Mercado",
        "Estratégia",
        "Conteúdo",
        "Revisão Criativa",
        "Redes Sociais"
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
        "nota_revisao": resultado.get("nota_revisao", 0),
        "tentativas_revisao": resultado.get("tentativas_revisao", 0),
        "tokens_usados": resultado.get("tokens_usados", 0),
    }

    json_data = json.dumps(campanha, indent=2, ensure_ascii=False)

    pdf = None
    conteudo_final = resultado.get("social", {}).get("conteudo", "")

    if conteudo_final:
        pdf = gerar_pdf(conteudo_final)

    # -----------------------------
    # Botões de exportação
    # -----------------------------
    st.subheader("Exportar campanha")

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "⬇️ Baixar JSON",
            data=json_data,
            file_name="campanha_marketing.json",
            mime="application/json"
        )

    with col2:
        if pdf:
            st.download_button(
                "📄 Baixar PDF",
                data=pdf,
                file_name="campanha_marketing.pdf",
                mime="application/pdf"
            )

    st.divider()

    # -----------------------------
    # Copiar conteúdo
    # -----------------------------
    st.subheader("Copiar conteúdo da campanha")

    st.text_area(
        "Texto da campanha",
        conteudo_final,
        height=250
    )

    st.divider()

    # -----------------------------
    # Nova campanha
    # -----------------------------
    if st.button("🔄 Gerar nova campanha"):
        st.session_state.resultado = None
        st.session_state.produto = ""
        st.rerun()
