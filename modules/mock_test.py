import streamlit as st
import json
import random


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
# START MOCK TEST
# -----------------------------
def start_mock_test(predicted_career, username):
    mock_data = load_json("data/mock_tests.json")
    progress_data = load_json("data/progress_data.json")

    if predicted_career not in mock_data:
        st.error("No mock test available for this career yet.")
        return

    questions = mock_data[predicted_career]

    # Unique session key for each user + career
    session_key = f"{username}_{predicted_career}_questions"

    # Generate new random questions every time button is clicked
    if st.button("Generate New Test"):
        st.session_state[session_key] = random.sample(
            questions,
            min(10, len(questions))
        )

        # Clear previous selected answers
        for i in range(10):
            answer_key = f"{username}_{predicted_career}_q{i}"
            if answer_key in st.session_state:
                del st.session_state[answer_key]

    # First load OR refresh if missing
    if session_key not in st.session_state:
        st.session_state[session_key] = random.sample(
            questions,
            min(10, len(questions))
        )

    selected_questions = st.session_state[session_key]

    st.subheader(f"{predicted_career} Mock Test")

    user_answers = []

    # Display questions
    for idx, q in enumerate(selected_questions):
        st.markdown(f"### Q{idx + 1}: {q['question']}")

        answer = st.radio(
            "Choose your answer:",
            q["options"],
            index=None,
            key=f"{username}_{predicted_career}_q{idx}"
        )

        user_answers.append(answer)

    # Submit test
    if st.button("Submit Test"):
        score = 0
        st.subheader("Results")

        for idx, q in enumerate(selected_questions):
            correct_answer = q["answer"]

            if user_answers[idx] == "Select an option":
                st.warning(f"Q{idx + 1}: Not answered.")
            elif user_answers[idx] == correct_answer:
                score += 1
                st.success(f"Q{idx + 1}: Correct!")
            else:
                st.error(
                    f"Q{idx + 1}: Incorrect. Correct answer: {correct_answer}"
                )

        st.metric(
            "Final Score",
            f"{score}/{len(selected_questions)}"
        )

        # Save progress
        if username in progress_data:
            if "mock_test_scores" not in progress_data[username]:
                progress_data[username]["mock_test_scores"] = {}

            if predicted_career not in progress_data[username]["mock_test_scores"]:
                progress_data[username]["mock_test_scores"][predicted_career] = []

            progress_data[username]["mock_test_scores"][predicted_career].append(score)

            save_json(
                "data/progress_data.json",
                progress_data
            )

        st.success("Mock test progress saved successfully!")