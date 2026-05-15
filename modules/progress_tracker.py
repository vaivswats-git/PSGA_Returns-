import streamlit as st
import json


# -----------------------------
# LOAD JSON DATA
# -----------------------------
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# -----------------------------
# DISPLAY USER PROGRESS
# -----------------------------
def show_progress(username):
    progress_data = load_json("data/progress_data.json")

    if username not in progress_data:
        st.error("No progress data found.")
        return

    user_progress = progress_data[username]

    st.title("Your Progress Tracker")

    # -----------------------------
    # MOCK TEST SCORES
    # -----------------------------
    st.subheader("Mock Test Performance")

    mock_scores = user_progress.get("mock_test_scores", {})

    if mock_scores:
        for career, scores in mock_scores.items():
            if scores:
                avg_score = sum(scores) / len(scores)

                st.metric(
                    label=f"{career} Average Score",
                    value=f"{avg_score:.2f}"
                )

                st.progress(
                    min(int((avg_score / 10) * 100), 100)
                )

    else:
        st.info("No mock test scores available yet.")

    # -----------------------------
    # COMPLETED COURSES
    # -----------------------------
    st.subheader("Completed Courses")

    completed_courses = user_progress.get("completed_courses", [])

    if completed_courses:
        for course in completed_courses:
            st.write(f"- {course}")
    else:
        st.info("No completed courses yet.")

    # -----------------------------
    # IMPROVED SKILLS
    # -----------------------------
    st.subheader("Skills Improved")

    skills_improved = user_progress.get("skills_improved", [])

    if skills_improved:
        for skill in skills_improved:
            st.write(f"- {skill}")
    else:
        st.info("No skills tracked yet.")

    # -----------------------------
    # CAREER HISTORY
    # -----------------------------
    st.subheader("Career Prediction History")

    career_history = user_progress.get("career_history", [])

    if career_history:
        for career in career_history:
            st.write(f"- {career}")
    else:
        st.info("No career history available.")