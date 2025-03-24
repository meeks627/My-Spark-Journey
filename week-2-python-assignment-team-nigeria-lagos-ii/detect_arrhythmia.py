# Find Abnormal Heart Rates (Loop & Condition)
# Filename: detect_arrhythmia.py
# Write a function `detect_arrhythmia(heart_rates)` that takes a list of heart rate readings
# and returns a list of values above 120 BPM or below 50 BPM.

def detect_arrhythmia(heart_rates):
    new_readings = []
    [new_readings.append(i) for i in heart_rates if i>120 or i<50]
    return new_readings
    # Implement function