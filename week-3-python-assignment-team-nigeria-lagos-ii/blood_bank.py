# Blood Bank Management System
# Filename: blood_bank.py
# Create a `BloodBank` class with:
# - `blood_type`
# - `units_available`
# Implement methods:
# - `donate_blood(units)` → Increases the units available.
# - `request_blood(units)` → Decreases units if enough stock exists.

class BloodBank():
    def __init__(self,blood_type,units_available):
        self.blood_type = blood_type
        self.units_available = units_available
    
    def donate_blood(self,units):
        self.units_available += units

    def request_blood(self,units):
        if self.units_available >= units:
            self.units_available -= units
        else:
            return "Insufficient Units"