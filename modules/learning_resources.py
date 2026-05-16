import json


def get_learning_resources(career_name):
    # Load jobs data
    with open("data/jobs.json", "r",encoding="utf-8") as jobs_file:
        jobs = json.load(jobs_file)

    # Load courses data
    with open("data/courses.json", "r",encoding="utf-8") as courses_file:
        courses = json.load(courses_file)

    resources = {}

    # Normalize career matching
    normalized_career = career_name.strip().lower()

    # Find matching career
    for job_name in jobs:
        if job_name.strip().lower() == normalized_career:
            required_skills = jobs[job_name]["required_skills"]

            # Match required skills with available courses
            for skill in required_skills:
                for course_skill in courses:
                    if skill.strip().lower() == course_skill.strip().lower():
                        resources[skill] = courses[course_skill]

            break

    return resources