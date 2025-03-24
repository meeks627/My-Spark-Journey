# NumPy: Normalize MRI Pixel Values
# Filename: normalize_mri.py
# Write a function `normalize_mri(image_array)` that normalizes pixel values in an MRI scan using NumPy.

import numpy as np
def normalize_mri(image_array):
    return (image_array - np.min(image_array))-(np.max(image_array)-np.min(image_array))
    pass  # Implement function