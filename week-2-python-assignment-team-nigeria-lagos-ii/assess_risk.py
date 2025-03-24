# Determine Patient Risk Level (Control Structures)
# Filename: assess_risk.py
# Write a function `assess_risk(age, bp, cholesterol)` that classifies a patient's cardiovascular risk
# based on their age, blood pressure, and cholesterol levels.

def assess_risk(age, bp, cholesterol):
    if age >= 60 or bp > 140 or cholesterol > 200:
        return "High"
    elif 40 <= age <= 60 or 130 < bp <= 140 or 180 < cholesterol <= 200:
        return "Moderate"
    else:
        return "Low"
    # Implement function