import json
import pickle
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder


# -----------------------------
# LOAD JOB DATA
# -----------------------------
with open("data/jobs.json", "r") as file:
    jobs_data = json.load(file)


# -----------------------------
# PREPARE TRAINING DATA
# -----------------------------
career_names = []
skill_sets = []

for career, details in jobs_data.items():
    career_names.append(career)
    skill_sets.append(details["required_skills"])


# -----------------------------
# ENCODE SKILLS
# -----------------------------
skill_encoder = MultiLabelBinarizer()
X = skill_encoder.fit_transform(skill_sets)


# -----------------------------
# ENCODE CAREERS
# -----------------------------
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(career_names)


# -----------------------------
# TRAIN MODEL
# -----------------------------
career_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

career_model.fit(X, y)


# -----------------------------
# SAVE MODEL FILES
# -----------------------------
with open("models/career_model.pkl", "wb") as file:
    pickle.dump(career_model, file)

with open("models/skill_encoder.pkl", "wb") as file:
    pickle.dump(skill_encoder, file)

with open("models/label_encoder.pkl", "wb") as file:
    pickle.dump(label_encoder, file)


print("Model training complete! All .pkl files generated successfully.")