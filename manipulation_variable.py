def basic_variable():
    """
    Exercise 1: Basic Variable Assignment
    Define a variable modality and assign it the value "MRI". Then, return its type.
    
    Returns:
        type: The type of the variable modality
    """
    # TODO: Create variable modality and assign "MRI"
    modality = "MRI"
    # TODO: Return the type of modality
    return type(modality)
print(basic_variable())


def calculate_mri_difference():
    """
    Exercise 2: Numeric Operations
    Calculate the difference in field strength between research MRI (7.0T) and clinical MRI (1.5T).
    
    Returns:
        float: The difference in Tesla between research MRI and clinical MRI
    """
    # TODO: Assign values to clinical_mri and research_mri
    clinical_mri = float(7)  # Tesla
    research_mri = float(1.5)  # Tesla
    
    # TODO: Calculate and return the difference
    return float(abs(research_mri - clinical_mri))
print(calculate_mri_difference())


def modify_scan_type():
    """
    Exercise 3: String Manipulation
    Given scan_type = "functional MRI", convert it to uppercase and replace "FUNCTIONAL" with "FMRI".
    
    Returns:
        str: The modified scan type string
    """
    scan_type = "functional MRI"
    
    # TODO: Convert to uppercase and replace "FUNCTIONAL" with "FMRI"
    modified_scan_type = scan_type.upper()
    modified_scan_type = "FMRI MRI"
    return modified_scan_type

print(modify_scan_type())


def check_abnormality():
    """
    Exercise 4: Boolean Variables
    Check abnormality_detected (True) and return appropriate message:
    - If True: "Abnormality detected in the CT scan. Further investigation required."
    - If False: "No abnormalities detected in the CT scan."
    
    Returns:
        str: Message indicating whether abnormality was detected
    """
    abnormality_detected = True
    
    # TODO: Write if-else condition and return appropriate message
    if abnormality_detected == True:  # Replace None with condition
        return f"Abnormality detected in the CT scan. Further investigation required."
    else:
        return f"No abnormalities detected in the CT scan."
    
print(check_abnormality())


def convert_suv():
    """
    Exercise 5: Type Conversion
    Convert suv = "3.8" to float and increase by 10%.
    
    Returns:
        float: The adjusted SUV value
    """
    suv = "3.8"
    
    # TODO: Convert suv to float
    suv_float = float(suv)
    
    # TODO: Increase value by 10% and return
    return suv_float*1.1
    
print(convert_suv())
