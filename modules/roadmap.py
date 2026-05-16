import streamlit as st
import json


# Load roadmap data
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# Get roadmap for predicted career
def get_roadmap(career_name):
    roadmaps = load_json("data/roadmaps.json")

    if career_name in roadmaps:
        return roadmaps[career_name]

    return ["No roadmap available for this career yet."]


# Display roadmap
def show_roadmap_tracker(username, predicted_career):
    roadmap_steps = get_roadmap(predicted_career)

    st.header(f"{predicted_career} Career Roadmap")
    st.subheader(f"Personalized roadmap for {username}")

    for idx, step in enumerate(roadmap_steps):
        st.write(f"Step {idx+1}: {step}")