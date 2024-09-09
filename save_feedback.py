# save_feedback.py

import json
import os

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