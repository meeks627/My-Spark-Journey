# Hospital Bed Allocation System
# Filename: hospital_bed.py
# Create a `HospitalBed` class with:
# - `bed_number`
# - `patient_name` (default `None`)
# Implement methods:
# - `assign_bed(patient_name)` → Assigns a patient to the bed.
# - `release_bed()` → Frees up the bed

class HospitalBed():
    def __init__(self,bed_number,patient_name):
        self.bed_number = bed_number 
        self.patient_name = None

    def assign_bed(self,patient_name):
        self.patient_name = patient_name
    
    def release_bed(self):
        self.patient_name = None