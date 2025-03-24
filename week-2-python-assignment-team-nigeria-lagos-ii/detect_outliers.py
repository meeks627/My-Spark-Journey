# NumPy: Detect Outlier Blood Pressures
# Filename: detect_outliers.py
# Write a function `detect_outliers(bp_array)` that identifies blood pressure outliers
# where values are more than 2 standard deviations away from the mean.
import numpy as np
def detect_outliers(bp_array):
    std_dev= np.std(bp_array)
    mean = np.mean(bp_array)
    outlier = mean + 2*std_dev
    return bp_array[bp_array> outlier]
    pass  # Implement function