import json


JOBS_FILE = "data/jobs.json"


# ----------------------------
# LOAD JOB DATA
# ----------------------------
def load_jobs():
    with open(JOBS_FILE, "r") as file:
        return json.load(file)


# ----------------------------
# ANALYZE SKILL GAP
# ----------------------------
def analyze_skill_gap(user_skills, predicted_career):
    jobs_data = load_jobs()

    if predicted_career not in jobs_data:
        return {
            "match_percentage": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    required_skills = jobs_data[predicted_career]["required_skills"]

    user_skills_set = set(skill.lower() for skill in user_skills)
    required_skills_set = set(skill.lower() for skill in required_skills)

    matched_skills = [
        skill for skill in required_skills
        if skill.lower() in user_skills_set
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill.lower() not in user_skills_set
    ]

    match_percentage = (
        len(matched_skills) / len(required_skills) * 100
        if required_skills else 0
    )

    return {
        "match_percentage": round(match_percentage, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }