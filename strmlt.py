import streamlit as st
from query_chatbot import query_chatbot
from feedback import initialize_json_files, handle_feedback
from st_auth import authenticate_user

"""
streamlit run strmlt.py
"""

# Define the file paths for the liked and disliked JSON files
liked_json_file_path = "feedback/liked_responses.json"
disliked_json_file_path = "feedback/disliked_responses.json"

def fetch_response():
    if st.session_state.user_input:
        query_text = st.session_state.user_input

        with st.spinner("Fetching response..."):
            response, sources = query_chatbot(query_text, st.session_state.chat_history)

        st.session_state.chat_history += f"<p><strong><big>User:</big></strong> {query_text}</p>"
        st.session_state.chat_history += f"<p><strong><big>Assistant:</big></strong> {response}</p><br>"

        st.session_state.current_query = query_text
        st.session_state.current_response = response
        st.session_state.user_input = ""

def main():
    if "chat_history" not in st.session_state:  st.session_state.chat_history = ""

    if "current_response" not in st.session_state:  st.session_state.current_response = ""

    if "current_query" not in st.session_state:  st.session_state.current_query = ""


    initialize_json_files()

    st.title("EWMS ChatBot")

    st.markdown(st.session_state.chat_history, unsafe_allow_html=True)
    st.text_input("You:", key="user_input", on_change=fetch_response)

    handle_feedback()


if __name__ == "__main__":
    main()
