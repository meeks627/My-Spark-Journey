# Reverse a Patient’s Name (String Manipulation)
# Filename: reverse_name.py
# Write a function `reverse_name(name)` that takes a patient’s full name and returns it reversed.

def reverse_name(name):
    name_list = list(name)
    reversed_list = name_list[::-1]
    reversed_name = "".join(reversed_list)
    return reversed_name 
    # Implement function