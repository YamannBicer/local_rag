import json
import os
import streamlit as st


# Define the file paths for the liked and disliked JSON files
liked_json_file_path = "feedback/liked_responses.json"
disliked_json_file_path = "feedback/disliked_responses.json"


# Ensure that the feedback directory and JSON files exist
def initialize_json_files():
    if not os.path.exists("feedback"):
        os.makedirs("feedback")

    if not os.path.exists(liked_json_file_path):
        with open(liked_json_file_path, "w") as file:
            json.dump([], file)  # Initialize with an empty list

    if not os.path.exists(disliked_json_file_path):
        with open(disliked_json_file_path, "w") as file:
            json.dump([], file)  # Initialize with an empty list


def save_feedback(query: str, response: str, like: bool):
    file_path = liked_json_file_path if like else disliked_json_file_path

    with open(file_path, "r") as file:
        data = json.load(file)

    data.append({
        "query": query,
        "response": response,
    })

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    st.success(f"Feedback saved to {'liked' if like else 'disliked'} responses!")