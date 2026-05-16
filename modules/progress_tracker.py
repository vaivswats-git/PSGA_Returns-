import streamlit as st
import json
import os


# -----------------------------
# LOAD JSON DATA
# -----------------------------
def load_json(file_path):
    if not os.path.exists(file_path):
        return {}

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


# -----------------------------
# SAVE JSON DATA
# -----------------------------
def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# -----------------------------
# DISPLAY USER PROGRESS
# -----------------------------
def show_progress(username):
    progress_data = load_json("data/progress_data.json")

    if username not in progress_data:
        progress_data[username] = {
            "mock_test_scores": {},
            "completed_courses": [],
            "skills_improved": [],
            "career_history": [],
            "course_proofs": {},
            "skill_proofs": {}
        }

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
    # COMPLETED COURSES + PROOF
    # -----------------------------
    st.subheader("Completed Courses")

    completed_courses = user_progress.get("completed_courses", [])
    course_proofs = user_progress.get("course_proofs", {})

    new_course = st.text_input("Add completed course")

    if st.button("Add Course"):
        if new_course.strip():
            completed_courses.append(new_course.strip())
            user_progress["completed_courses"] = completed_courses

    for course in completed_courses:
        st.write(f"- {course}")

        proof_text = st.text_input(
            f"Proof for {course}",
            value=course_proofs.get(course, {}).get("proof_text", ""),
            key=f"course_{course}"
        )

        uploaded_file = st.file_uploader(
            f"Upload proof file for {course}",
            type=["pdf", "png", "jpg", "jpeg"],
            key=f"course_file_{course}"
        )

        proof_file_path = course_proofs.get(course, {}).get("proof_file", "")

        if uploaded_file:
            os.makedirs("proofs", exist_ok=True)

            file_extension = uploaded_file.name.split(".")[-1]
            proof_file_path = f"proofs/{username}_{course}.{file_extension}"

            with open(proof_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        course_proofs[course] = {
            "proof_text": proof_text,
            "proof_file": proof_file_path
        }

    user_progress["course_proofs"] = course_proofs

    # -----------------------------
    # SKILLS IMPROVED + PROOF
    # -----------------------------
    st.subheader("Skills Improved")

    skills_improved = user_progress.get("skills_improved", [])
    skill_proofs = user_progress.get("skill_proofs", {})

    new_skill = st.text_input("Add improved skill")

    if st.button("Add Skill"):
        if new_skill.strip():
            skills_improved.append(new_skill.strip())
            user_progress["skills_improved"] = skills_improved

    for skill in skills_improved:
        st.write(f"- {skill}")

        proof_text = st.text_input(
            f"Proof for {skill}",
            value=skill_proofs.get(skill, {}).get("proof_text", ""),
            key=f"skill_{skill}"
        )

        uploaded_file = st.file_uploader(
            f"Upload proof file for {skill}",
            type=["pdf", "png", "jpg", "jpeg"],
            key=f"skill_file_{skill}"
        )

        proof_file_path = skill_proofs.get(skill, {}).get("proof_file", "")

        if uploaded_file:
            os.makedirs("proofs", exist_ok=True)

            file_extension = uploaded_file.name.split(".")[-1]
            proof_file_path = f"proofs/{username}_{skill}.{file_extension}"

            with open(proof_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        skill_proofs[skill] = {
            "proof_text": proof_text,
            "proof_file": proof_file_path
        }

    user_progress["skill_proofs"] = skill_proofs

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

    # -----------------------------
    # SAVE UPDATED DATA
    # -----------------------------
    progress_data[username] = user_progress
    save_json("data/progress_data.json", progress_data)

    st.success("Progress updated successfully!")