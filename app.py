import streamlit as st
from chain import build_chain

st.set_page_config(page_title="FAQ - História do Brasil 🇧🇷")

st.title("📚 FAQ - História do Brasil 🇧🇷")
st.write("Digite sua pergunta sobre História do Brasil:")

pergunta = st.text_input("Sua pergunta:")

if pergunta:
    chain = build_chain()
    with st.spinner("Pensando..."):
        resposta = chain.run(question=pergunta)
    st.markdown("### 📖 Resposta:")
    st.write(resposta)