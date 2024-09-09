import streamlit as st
from query_chatbot import query_chatbot
import json
import os
from save_feedback import initialize_json_files, save_feedback
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

        # Format the chat history so that the user and assistant messages are shown on separate lines with bold headings
        st.session_state.chat_history += f"<p><strong><big>User:</big></strong> {query_text}</p>"
        st.session_state.chat_history += f"<p><strong><big>Assistant:</big></strong> {response}</p><br>"

        st.session_state.current_query = query_text
        st.session_state.current_response = response
        st.session_state.user_input = ""


def main():
    # Initialize session state variables if they don't exist
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = ""
    if "current_response" not in st.session_state:
        st.session_state.current_response = ""
    if "current_query" not in st.session_state:
        st.session_state.current_query = ""

    initialize_json_files()

    st.title("EWMS ChatBot")

    # Display the chat history formatted with HTML tags for bold and large text
    st.markdown(st.session_state.chat_history, unsafe_allow_html=True)

    st.text_input("You:", key="user_input", on_change=fetch_response)

    if st.session_state.current_response:
        st.write("Do you like the response?")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("👍 Like"):
                save_feedback(st.session_state.current_query, st.session_state.current_response, like=True)

        with col2:
            if st.button("👎 Dislike"):
                save_feedback(st.session_state.current_query, st.session_state.current_response, like=False)


if __name__ == "__main__":
    main()
