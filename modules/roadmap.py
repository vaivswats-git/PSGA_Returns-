# -----------------------------
# ROADMAP TRACKER WITH LOCKED STEPS + PROOF UPLOAD
# -----------------------------
import streamlit as st
import json
import os


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
# GET ROADMAP
# -----------------------------
def get_roadmap(career_name):
    roadmaps = load_json("data/roadmaps.json")

    if career_name in roadmaps:
        return roadmaps[career_name]

    return ["No roadmap available for this career yet."]


# -----------------------------
# SHOW INTERACTIVE ROADMAP
# -----------------------------
def show_roadmap_tracker(username, predicted_career):
    roadmap_steps = get_roadmap(predicted_career)
    progress_data = load_json("data/progress_data.json")

    # Ensure user roadmap progress exists
    if "roadmap_progress" not in progress_data[username]:
        progress_data[username]["roadmap_progress"] = {}

    if predicted_career not in progress_data[username]["roadmap_progress"]:
        progress_data[username]["roadmap_progress"][predicted_career] = [
            {
                "completed": False,
                "proof_text": "",
                "proof_file": ""
            }
            for _ in roadmap_steps
        ]

    user_progress = progress_data[username]["roadmap_progress"][predicted_career]

    st.header(f"{predicted_career} Career Roadmap")

    completed_count = 0

    # Create proofs folder
    os.makedirs("proofs", exist_ok=True)

    for idx, step in enumerate(roadmap_steps):

        # Lock future steps until previous completed
        if idx > 0 and not user_progress[idx - 1]["completed"]:
            st.warning(f"🔒 Step {idx+1} locked. Complete previous step first.")
            break

        st.subheader(f"Step {idx+1}: {step}")

        completed = st.checkbox(
            "Mark as completed",
            value=user_progress[idx]["completed"],
            key=f"{username}_{predicted_career}_step_{idx}"
        )

        proof_text = st.text_input(
            "Enter proof/notes (course name, GitHub link, certificate details, etc.)",
            value=user_progress[idx]["proof_text"],
            key=f"{username}_{predicted_career}_proof_{idx}"
        )

        uploaded_file = st.file_uploader(
            "Upload proof file/image (PDF, JPG, PNG)",
            type=["pdf", "png", "jpg", "jpeg"],
            key=f"{username}_{predicted_career}_file_{idx}"
        )

        proof_file_path = user_progress[idx]["proof_file"]

        if uploaded_file:
            file_extension = uploaded_file.name.split(".")[-1]
            proof_file_path = f"proofs/{username}_{predicted_career}_step_{idx}.{file_extension}"

            with open(proof_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        # Validation:
        # Cannot complete unless proof text OR file exists
        if completed:
            if proof_text.strip() or proof_file_path:
                user_progress[idx]["completed"] = True
                user_progress[idx]["proof_text"] = proof_text
                user_progress[idx]["proof_file"] = proof_file_path
                completed_count += 1
                st.success("✅ Step verified and unlocked.")
            else:
                user_progress[idx]["completed"] = False
                st.error("⚠ Please provide proof before completing this step.")
        else:
            user_progress[idx]["completed"] = False
            user_progress[idx]["proof_text"] = proof_text
            user_progress[idx]["proof_file"] = proof_file_path

    # Save updated progress
    progress_data[username]["roadmap_progress"][predicted_career] = user_progress
    save_json("data/progress_data.json", progress_data)

    # Progress bar
    progress_percent = completed_count / len(roadmap_steps)
    st.progress(progress_percent)

    st.info(
        f"Roadmap Completion: {completed_count}/{len(roadmap_steps)} steps completed"
    )