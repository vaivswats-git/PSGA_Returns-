import streamlit as st
import json

from modules.career import predict_career
from modules.skill_gap import analyze_skill_gap
from modules.learning_resources import get_learning_resources
from modules.roadmap import show_roadmap_tracker
from modules.mock_test import start_mock_test
from modules.progress_tracker import show_progress
from modules.streak import show_streak, update_streak


# -----------------------------
# LOAD JSON DATA
# -----------------------------
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# -----------------------------
# DASHBOARD PAGE
# -----------------------------
def dashboard_page(username):

    users = load_json("data/users.json")
    companies_data = load_json("data/companies.json")

    user = users[username]

    # Update streak on login
    update_streak(username)

    st.title(f" Welcome, {user['name']}!")
    st.markdown("### Your personalized growth dashboard")

    # -----------------------------
    # SIDEBAR NAVIGATION
    # -----------------------------
    st.sidebar.title(" Dashboard Navigation")

    section = st.sidebar.radio(
        "Choose Section",
        [
            "Career Prediction",
            "Skill Gap Analysis",
            "Learning Resources",
            "Mock Test",
            "Roadmap",
            "Progress Tracker",
            "Streak Tracker"
        ]
    )

    # -----------------------------
    # CAREER PREDICTION
    # -----------------------------
    if section == "Career Prediction":
        st.header("Career Prediction")

        # Show current skills
        st.subheader("Your Current Skills")
        st.write(", ".join(user["skills"]))

        # Skill editing
        updated_skills = st.text_area(
            "Edit your skills (comma separated)",
            value=", ".join(user["skills"])
        )

        if st.button("Update Skills"):
            new_skills = [
                skill.strip()
                for skill in updated_skills.split(",")
                if skill.strip()
            ]

            user["skills"] = new_skills

            users["skills"] = new_skills

            with open("users.json", "w", encoding="utf-8") as file:
                json.dump({"users": users}, file, indent=4)

            st.success("Skills updated successfully!")

    # Predict updated career
    predicted_career = predict_career(user["skills"])

    st.success(f"Predicted Career Path: {predicted_career}")

    # Recommended companies
    st.subheader("Recommended Companies")

    if predicted_career in companies_data:
        cols = st.columns(3)

        for idx, company in enumerate(companies_data[predicted_career]):
            with cols[idx % 3]:
                st.info(company)
    # -----------------------------
# SKILL GAP ANALYSIS
# -----------------------------
    elif section == "Skill Gap Analysis":
        st.header(" Skill Gap Analysis")

        predicted_career = predict_career(user["skills"])

        missing_skills = analyze_skill_gap(
            user["skills"],
            predicted_career
        )

        if missing_skills:

            st.info(f"Match Percentage: {missing_skills['match_percentage']}%")

            st.subheader("Matched Skills")
            for skill in missing_skills["matched_skills"]:
                st.success(skill)

            st.subheader("Missing Skills You Should Learn")
            for skill in missing_skills["missing_skills"]:
                st.error(skill)

        else:
            st.success("You already strongly match this career!")
    # -----------------------------
    # LEARNING RESOURCES
    # -----------------------------
    elif section == "Learning Resources":
        st.header(" Learning Resources")

        predicted_career = predict_career(user["skills"])

        resources = get_learning_resources(predicted_career)

        if resources:
            for skill, resource_data in resources.items():
                with st.expander(skill):

                    st.write(resource_data["title"])

                    st.link_button(
                        f"Open Free Course for {skill}",
                        resource_data["link"]
                    )
        else:
            st.warning("No learning resources available for this career yet.")
    # -----------------------------
    # MOCK TEST
    # -----------------------------
    elif section == "Mock Test":
        st.header(" Mock Test")

        predicted_career = predict_career(user["skills"])

        start_mock_test(
            predicted_career,
            username
        )

    # -----------------------------
    # ROADMAP
    # -----------------------------
    elif section == "Roadmap":
        st.header(" Career Roadmap")

        predicted_career = predict_career(user["skills"])

        show_roadmap_tracker(username,predicted_career)

    # -----------------------------
    # PROGRESS TRACKER
    # -----------------------------
    elif section == "Progress Tracker":
        show_progress(username)

    # -----------------------------
    # STREAK TRACKER
    # -----------------------------
    elif section == "Streak Tracker":
        show_streak(username)