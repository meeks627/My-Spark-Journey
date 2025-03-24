# Detect COVID Symptoms (Functions & Lists)
# Filename: covid_symptoms_checker.py
# Write a function `covid_symptoms_checker(symptoms)` that checks if a patient has at least
# two of these symptoms: "fever", "cough", "fatigue", "loss of taste", "difficulty breathing".
# Return "Likely COVID" or "Unlikely COVID".

def covid_symptoms_checker(symptoms):
    list_of_symptoms = ["fever", "cough", "fatigue", "loss of taste", "difficulty breathing"]
    if len(set(list_of_symptoms) & set(symptoms))>= 3:
        return "Likely COVID"
    else:
        return "Unlikely COVID"
        # Implement function