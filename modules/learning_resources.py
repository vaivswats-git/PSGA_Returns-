import json


def get_learning_resources(career_name):
    with open("data/courses.json", "r") as file:
        courses = json.load(file)

    if career_name in courses:
        return courses[career_name]

    return {}