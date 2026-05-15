import streamlit as st
import json


USERS_FILE = "data/users.json"


# -----------------------------
# LOAD USERS
# -----------------------------
def load_users():
    with open(USERS_FILE, "r") as file:
        return json.load(file)


# -----------------------------
# SAVE USERS
# -----------------------------
def save_users(users_data):
    with open(USERS_FILE, "w") as file:
        json.dump(users_data, file, indent=4)


# -----------------------------
# PROFILE SETUP PAGE
# -----------------------------
def profile_setup_page():
    st.title("Complete Your Profile")

    username = st.session_state.username

    users = load_users()

    full_name = st.text_input("Full Name")

    career_goal = st.selectbox(
        "Select Career Goal",
        [
        "Data Science",
        "Web Development",
        "AI/ML",
        "Cybersecurity",
        "Software Engineering",
        "Doctor",
        "Nurse",
        "Psychologist",
        "Lawyer",
        "Teacher",
        "Professor",
        "Chartered Accountant",
        "Investment Banker",
        "Entrepreneur",
        "Digital Marketing",
        "Content Creator",
        "Graphic Designer",
        "Fashion Designer",
        "Chef",
        "Hotel Management",
        "Journalist",
        "Civil Services",
        "Pilot",
        "Fitness Trainer",
        "Photographer",
        "Musician",
        "Actor",
        "Social Worker",
        "Event Manager",
        "Real Estate Agent"
        ]
    )

    available_skills = [
        "Python", "SQL", "Machine Learning", "Statistics", "Pandas", "Data Visualization",
    "HTML", "CSS", "JavaScript", "React", "Node.js", "Databases",
    "Deep Learning", "TensorFlow", "NLP", "Mathematics",
    "Networking", "Linux", "Ethical Hacking", "Cryptography", "Security Tools",
    "Java", "Data Structures", "Algorithms", "System Design",
    "Medical Knowledge", "Diagnosis", "Patient Care", "Surgery Basics", "Critical Thinking",
    "Medical Procedures", "Emergency Response", "Empathy", "Record Keeping",
    "Counseling", "Behavior Analysis", "Research", "Mental Health Assessment",
    "Legal Research", "Argumentation", "Public Speaking", "Negotiation", "Documentation",
    "Subject Knowledge", "Lesson Planning", "Classroom Management", "Patience", "Assessment",
    "Academic Writing", "Mentorship", "Curriculum Design",
    "Accounting", "Taxation", "Auditing", "Financial Reporting", "Excel", "Compliance",
    "Finance", "Market Analysis", "Valuation", "Risk Assessment",
    "Leadership", "Business Strategy", "Problem Solving",
    "SEO", "Social Media", "Content Marketing", "Branding", "Analytics", "Advertising",
    "Video Editing", "Creativity", "Storytelling",
    "Photoshop", "Illustrator", "Typography", "UI Basics",
    "Textile Knowledge", "Sketching", "Trend Analysis", "Sewing",
    "Cooking", "Recipe Development", "Time Management", "Presentation", "Food Safety",
    "Hospitality", "Customer Service", "Management", "Event Planning",
    "Writing", "Interviewing", "Editing",
    "General Knowledge", "Policy Understanding", "Administration",
    "Aviation Knowledge", "Navigation", "Decision Making", "Technical Skills", "Discipline",
    "Exercise Science", "Nutrition", "Motivation", "Physical Fitness", "Planning",
    "Camera Skills", "Lighting",
    "Instrument Mastery", "Performance", "Composition", "Practice Discipline", "Collaboration",
    "Emotional Intelligence", "Public Presence",
    "Community Outreach", "Advocacy",
    "Budgeting",
    "Sales", "Market Knowledge"
    ]

    selected_skills = st.multiselect(
        "Select Your Current Skills",
        available_skills
    )

    if st.button("Save Profile"):
        users[username]["name"] = full_name
        users[username]["career_goal"] = career_goal
        users[username]["skills"] = selected_skills

        save_users(users)

        st.session_state.profile_completed = True

        st.success("Profile setup completed!")
        st.rerun()