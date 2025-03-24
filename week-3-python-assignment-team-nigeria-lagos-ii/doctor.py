# Doctor Information System
# Filename: doctor.py
# Create a `Doctor` class with:
# - `name`
# - `specialization`
# - `patients` (list)
# Implement methods:
# - `add_patient(patient_name)` → Adds a patient's name to the list.
# - `list_patients()` → Returns all assigned patients.

class Doctor():
    def __init__(self, name, specialization):
        self.name = name
        self.specialization= specialization
        self.patients = []

    def add_patients(self,patient_name):
        self.patients.append(patient_name)

    def list_patients(self):
        return self.patients