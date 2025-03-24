# Average Tumor Size (Loops & Lists)
# Filename: average_tumor_size.py
# Write a function `average_tumor_size(sizes)` that calculates the average tumor size from a list of measurements.

def average_tumor_size(sizes):
    sum = 0
    length = len(sizes)
    for i in sizes:
        sum+=i
    average = sum / length
    return average
      # Implement function