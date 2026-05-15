import json


COMPANIES_FILE = "data/companies.json"


# ----------------------------
# LOAD COMPANY DATA
# ----------------------------
def load_companies():
    with open(COMPANIES_FILE, "r") as file:
        return json.load(file)


# ----------------------------
# GET COMPANY RECOMMENDATIONS
# ----------------------------
def get_company_recommendations(predicted_career):
    companies_data = load_companies()

    recommendations = []

    for company, details in companies_data.items():
        if details["domain"].lower() == predicted_career.lower():
            recommendations.append({
                "company_name": company,
                "required_skills": details["required_skills"]
            })

    return recommendations