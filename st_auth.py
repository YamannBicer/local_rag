import streamlit as st

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