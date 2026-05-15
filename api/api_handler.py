import requests
import random
import json


# ----------------------------
# API CONFIGURATION
# ----------------------------
QUIZ_API_URL = "https://opentdb.com/api.php"


# ----------------------------
# CAREER TO CATEGORY MAP
# ----------------------------
career_category_map = {
    "Data Science": "18",
    "Web Development": "18",
    "AI/ML": "18",
    "Cybersecurity": "18",
    "Software Engineering": "18",
    "Doctor": "17",
    "Nurse": "17",
    "Psychologist": "17",
    "Lawyer": "9",
    "Teacher": "9",
    "Professor": "9",
    "Chartered Accountant": "23",
    "Investment Banker": "23",
    "Entrepreneur": "23",
    "Digital Marketing": "9",
    "Content Creator": "9",
    "Graphic Designer": "25",
    "Fashion Designer": "25",
    "Chef": "9",
    "Hotel Management": "9",
    "Journalist": "9",
    "Civil Services": "9",
    "Pilot": "17",
    "Fitness Trainer": "17",
    "Photographer": "25",
    "Musician": "12",
    "Actor": "11",
    "Social Worker": "9",
    "Event Manager": "9",
    "Real Estate Agent": "23"
}


# ----------------------------
# LOAD LOCAL FALLBACK QUESTIONS
# ----------------------------
def load_local_mock_tests():
    try:
        with open("data/mock_tests.json", "r") as file:
            return json.load(file)
    except:
        return {}


# ----------------------------
# FETCH QUESTIONS FROM API
# ----------------------------
def fetch_api_questions(predicted_career, num_questions=10):
    category = career_category_map.get(predicted_career, "9")

    params = {
        "amount": num_questions,
        "category": category,
        "type": "multiple"
    }

    try:
        response = requests.get(QUIZ_API_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            questions = []

            for item in data["results"]:
                options = item["incorrect_answers"] + [item["correct_answer"]]
                random.shuffle(options)

                questions.append({
                    "question": item["question"],
                    "options": options,
                    "answer": item["correct_answer"]
                })

            return questions

    except:
        return []

    return []


# ----------------------------
# MAIN FETCH FUNCTION
# ----------------------------
def get_mock_questions(predicted_career, num_questions=10):
    # Try API first
    api_questions = fetch_api_questions(predicted_career, num_questions)

    if api_questions:
        return api_questions

    # Fallback to local JSON
    local_data = load_local_mock_tests()

    if predicted_career in local_data:
        return random.sample(
            local_data[predicted_career],
            min(num_questions, len(local_data[predicted_career]))
        )

    return []