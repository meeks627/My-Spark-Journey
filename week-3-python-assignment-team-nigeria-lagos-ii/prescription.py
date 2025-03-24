# Pharmacy Prescription System
# Filename: prescription.py
# Create a `Prescription` class with:
# - `patient_name`
# - `medications` (dictionary with drug names as keys and dosages as values)
# Implement methods:
# - `add_medication(drug, dosage)` → Adds a drug and dosage.
# - `view_prescription()` → Displays all prescribed medications.

class Prescription():
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.medications = {}

    def add_medication(self, drug, dosage):
        self.medications.update({drug : dosage})

    def view_prescription(self):
        return self.medications