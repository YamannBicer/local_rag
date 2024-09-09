# strmlt_best_matches.py
import streamlit as st
from query_best_matches import query_best_matches

def fetch_best_matches():
    if st.session_state.user_input:
        query_text = st.session_state.user_input

        with st.spinner("Fetching best matches..."):
            best_matches, matches_df = query_best_matches(query_text)

        if isinstance(best_matches, str):
            st.session_state.chat_history += f"<p><strong><big>User:</big></strong> {query_text}</p>"
            st.session_state.chat_history += f"<p><strong><big>Assistant:</big></strong> {best_matches}</p><br>"
        else:
            st.session_state.chat_history += f"<p><strong><big>User:</big></strong> {query_text}</p>"
            st.session_state.chat_history += f"<p><strong><big>Assistant:</big></strong> The 5 most likely data names are:</p>"
            for i, name in enumerate(best_matches, 1):
                st.session_state.chat_history += f"<p>{i}. {name}</p>"
            st.session_state.chat_history += "<br>"

        st.session_state.current_query = query_text
        st.session_state.user_input = ""

def main():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = ""
    if "current_query" not in st.session_state:
        st.session_state.current_query = ""

    st.title("Best Matches Finder")

    st.markdown(st.session_state.chat_history, unsafe_allow_html=True)

    st.text_input("You:", key="user_input", on_change=fetch_best_matches)

if __name__ == "__main__":
    main()