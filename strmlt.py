import streamlit as st
from query_chatbot import query_chatbot

"""
streamlit run strmlt.py
"""

def fetch_response():
    if st.session_state.user_input:
        query_text = st.session_state.user_input

        with st.spinner("Fetching response..."):
            response, sources = query_chatbot(query_text, st.session_state.chat_history)

        st.session_state.chat_history += f"User: {query_text}\nAssistant: {response}\n\n"
        # st.session_state.display_history  += f"User: {query_text}\n\nChatBot: {response}\n\nSources: {sources}\n\n"

        st.session_state.user_input = ""

def main():
    # Initialize session state variables if they don't exist
    # if "display_history" not in st.session_state: st.session_state.display_history = ""
    if "chat_history" not in st.session_state: st.session_state.chat_history = ""


    st.title("EWMS ChatBot")

    st.markdown(st.session_state.display_history)

    # Text input for the user's question with a callback to process input
    st.text_input("You:", key="user_input", on_change=fetch_response)


if __name__ == "__main__":
    main()
