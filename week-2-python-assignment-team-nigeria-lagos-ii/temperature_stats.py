# NumPy: Compute Patient Temperature Stats
# Filename: temperature_stats.py
# Write a function `temperature_stats(temps)` that takes a NumPy array of temperature readings
# and returns the mean, max, and min temperature.

import numpy as np
def temperature_stats(temps):
    temps_mean = np.mean(temps)
    temps_max = np.max(temps)
    temps_min = np.min(temps)
    return  temps_mean, temps_max, temps_min
    pass  # Implement function