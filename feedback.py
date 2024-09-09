import json
import os
import streamlit as st

def handle_feedback():
    if st.session_state.current_response:
        st.write("Do you like the response?")
        col1, col2 = st.columns(2)

        # Initialize feedback_given state if not present
        if "feedback_given" not in st.session_state:
            st.session_state.feedback_given = False


        with col1:
            # Disable the "Like" button if any feedback has been given
            if st.button("👍 Like", disabled=st.session_state.feedback_given):
                save_feedback(st.session_state.current_query, st.session_state.current_response, like=True, user="user")
                st.success("You liked the response!")
                st.session_state.liked = True
                st.session_state.disliked = False
                st.session_state.feedback_given = True  # Disable both buttons

        with col2:
            # Disable the "Dislike" button if any feedback has been given
            if st.button("👎 Dislike", disabled=st.session_state.feedback_given):
                save_feedback(st.session_state.current_query, st.session_state.current_response, like=False, user="user")
                st.error("You disliked the response!")
                st.session_state.liked = False
                st.session_state.disliked = True
                st.session_state.feedback_given = True  # Disable both buttons

def initialize_json_files():
    liked_json_file_path = "feedback/liked_responses.json"
    disliked_json_file_path = "feedback/disliked_responses.json"
    if not os.path.exists(liked_json_file_path):
        with open(liked_json_file_path, 'w') as f:
            json.dump([], f)
    if not os.path.exists(disliked_json_file_path):
        with open(disliked_json_file_path, 'w') as f:
            json.dump([], f)

def save_feedback(query, response, like, user):
    feedback = {
        "user": user,
        "query": query,
        "response": response
    }
    file_path = "feedback/liked_responses.json" if like else "feedback/disliked_responses.json"
    with open(file_path, 'r+') as f:
        data = json.load(f)
        data.append(feedback)
        f.seek(0)
        json.dump(data, f, indent=4)

def reset_feedback_state():
    st.session_state.liked = False
    st.session_state.disliked = False
    st.session_state.feedback_given = False

# Reset feedback state when a new response is fetched
if st.session_state.get("current_response"):
    reset_feedback_state()