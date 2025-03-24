# Organ Transplant Waiting List
# Filename: transplant_waitlist.py
# Create a `TransplantWaitingList` class with:
# - `organ` (e.g., kidney, liver)
# - `patients` (list of names)
# Implement methods:
# - `add_patient(name)` → Adds a patient to the waiting list.
# - `remove_patient(name)` → Removes a patient when they receive a transplant.

class TransplantWaitingList():
    def __init__(self, organ):
        self.organ = organ
        self.patients = []

    def add_patient(self,name):
        self.patients.append(name)

    def remove_patient(self,name):
        self.patients.remove(name)