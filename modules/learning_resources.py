import json


def get_learning_resources(career_name):
    with open("data/courses.json", "r") as file:
        courses = json.load(file)

    career_name=career_name.strip()
    for career in courses:
        if career.strip().lower() == career_name.lower():
            return courses[career]
        return {}
