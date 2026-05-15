def clean_input_list(input_text):
    return [
        item.strip()
        for item in input_text.split(",")
        if item.strip()
    ]


def format_skills_for_display(skills):
    return ", ".join(skills)