import streamlit as st
from query_chatbot import query_chatbot
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

        st.session_state.chat_history += f"<p><strong><big>User:</big></strong> {query_text}</p>"
        st.session_state.chat_history += f"<p><strong><big>Assistant:</big></strong> {response}</p><br>"

        st.session_state.current_query = query_text
        st.session_state.current_response = response
        st.session_state.user_input = ""

def authenticate_user():
    username = st.text_input("Username")
    if st.button("Login"):
        # Simple authentication logic (replace with actual authentication)
        if username:
            st.session_state.logged_in_user = username
            return True
        else:
            st.error("Please enter a username")
            return False
    return False

def handle_feedback():
    if st.session_state.current_response:
        st.write("Do you like the response?")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("👍 Like"):
                save_feedback(st.session_state.current_query, st.session_state.current_response, like=True, user=st.session_state.logged_in_user)

        with col2:
            if st.button("👎 Dislike"):
                save_feedback(st.session_state.current_query, st.session_state.current_response, like=False, user=st.session_state.logged_in_user)

def main():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = ""
    if "current_response" not in st.session_state:
        st.session_state.current_response = ""
    if "current_query" not in st.session_state:
        st.session_state.current_query = ""
    if "logged_in_user" not in st.session_state:
        st.session_state.logged_in_user = None

    initialize_json_files()

    st.title("EWMS ChatBot")

    if st.session_state.logged_in_user:
        st.markdown(f"**Logged in as:** {st.session_state.logged_in_user}")
        st.markdown(st.session_state.chat_history, unsafe_allow_html=True)
        st.text_input("You:", key="user_input", on_change=fetch_response)

        handle_feedback()

    else:
        if authenticate_user():
            st.experimental_rerun()  # Rerun the app after successful login to refresh the view

if __name__ == "__main__":
    main()
