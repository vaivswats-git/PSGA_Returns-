import json
import os


USERS_FILE = "data/users.json"


# -----------------------------
# LOAD USERS
# -----------------------------
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, "r") as file:
        return json.load(file)


# -----------------------------
# SAVE USERS
# -----------------------------
def save_users(users_data):
    with open(USERS_FILE, "w") as file:
        json.dump(users_data, file, indent=4)


# -----------------------------
# SIGNUP FUNCTION
# -----------------------------
def signup_user(username, email, password):
    users = load_users()

    if username in users:
        return False

    users[username] = {
        "name": username,
        "email": email,
        "password": password,
        "career_goal": "",
        "skills": [],
        "completed_courses": [],
        "mock_test_scores": {},
        "roadmap_progress": {},
        "streak": 0,
        "last_active": "",
        "created_at": "2026-05-06"
    }

    save_users(users)
    return True


# -----------------------------
# LOGIN FUNCTION
# -----------------------------
def login_user(username, password):
    users = load_users()

    if username not in users:
        return False

    return users[username]["password"] == password