import streamlit as st
from query_chatbot import query_chatbot

"""
streamlit run strmlt.py
"""

# Streamlit app
st.title("ChatBot with Streamlit Interface")

query_text = st.text_input("Message ChatBot:", "")

if query_text:
    with st.spinner("Fetching response..."):
        response, sources = query_chatbot(query_text)

    st.subheader("Response:")
    st.write(response)

    st.subheader("Sources:")
    for source in sources:
        st.write(source)
