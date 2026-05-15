import streamlit as st
import json
from datetime import datetime


# -----------------------------
# LOAD JSON DATA
# -----------------------------
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# -----------------------------
# SAVE JSON DATA
# -----------------------------
def save_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


# -----------------------------
# UPDATE USER STREAK
# -----------------------------
def update_streak(username):
    streak_data = load_json("data/streak_data.json")

    if username not in streak_data:
        streak_data[username] = {
            "current_streak": 0,
            "longest_streak": 0,
            "last_active_date": "",
            "total_active_days": 0
        }

    today = datetime.today().date()
    last_active = streak_data[username]["last_active_date"]

    # First login
    if not last_active:
        streak_data[username]["current_streak"] = 1
        streak_data[username]["longest_streak"] = 1
        streak_data[username]["total_active_days"] = 1

    else:
        last_date = datetime.strptime(
            last_active,
            "%Y-%m-%d"
        ).date()

        difference = (today - last_date).days

        if difference == 1:
            streak_data[username]["current_streak"] += 1
            streak_data[username]["total_active_days"] += 1

        elif difference > 1:
            streak_data[username]["current_streak"] = 1
            streak_data[username]["total_active_days"] += 1

    # Update longest streak
    if streak_data[username]["current_streak"] > streak_data[username]["longest_streak"]:
        streak_data[username]["longest_streak"] = streak_data[username]["current_streak"]

    streak_data[username]["last_active_date"] = str(today)

    save_json("data/streak_data.json", streak_data)


# -----------------------------
# DISPLAY STREAK DASHBOARD
# -----------------------------
def show_streak(username):
    streak_data = load_json("data/streak_data.json")

    if username not in streak_data:
        st.info("No streak data available yet.")
        return

    user_streak = streak_data[username]

    st.title("Your Learning Streak")

    st.metric(
        "Current Streak",
        f"{user_streak['current_streak']} days"
    )

    st.metric(
        "Longest Streak",
        f"{user_streak['longest_streak']} days"
    )

    st.metric(
        "Total Active Days",
        f"{user_streak['total_active_days']} days"
    )

    progress_percent = min(
        user_streak["current_streak"] * 10,
        100
    )

    st.progress(progress_percent)