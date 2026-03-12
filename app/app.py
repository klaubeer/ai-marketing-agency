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

    with st.spinner("Executando agentes de marketing..."):

        resultado = grafo.invoke(estado_inicial)

    st.success("Campanha gerada!")

    st.divider()

    st.header("📱 Campanha Final")

    st.markdown(resultado["social"]["conteudo"])

    st.divider()

    st.metric(
        label="Tokens utilizados",
        value=resultado["tokens_usados"]
    )
