import pickle
import numpy as np


# ----------------------------
# LOAD MODELS
# ----------------------------
with open("models/career_model.pkl", "rb") as f:
    career_model = pickle.load(f)

with open("models/skill_encoder.pkl", "rb") as f:
    skill_encoder = pickle.load(f)

with open("models/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)


# ----------------------------
# PREPROCESS USER SKILLS
# ----------------------------
def preprocess_skills(user_skills):
    skill_vector = np.zeros(len(skill_encoder.classes_))

    for skill in user_skills:
        skill = skill.strip()

        if skill in skill_encoder.classes_:
            index = list(skill_encoder.classes_).index(skill)
            skill_vector[index] = 1

    return skill_vector.reshape(1, -1)


# ----------------------------
# PREDICT CAREER
# ----------------------------
def predict_career(user_skills):
    processed_skills = preprocess_skills(user_skills)

    prediction = career_model.predict(processed_skills)

    predicted_career = label_encoder.inverse_transform(prediction)[0]

    return predicted_career