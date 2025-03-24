def scan_type_classification():
    """
    Given modality = "MRI", write an if-elif-else statement that prints:                  
    "Magnetic Resonance Imaging" for "MRI",
    "Computed Tomography" for "CT",
    "Other imaging modality" otherwise.
    
    Returns:
        str: The classification of the imaging modality.
    """
    modality = "MRI"
    if modality == "MRI":
        return("Magnetic Resonance Imaging")
    elif modality == "CT":
        return("Computed Tomography")
    else:
        return("Other imaging modality")

print(scan_type_classification())


def patient_risk_level():
    """
    Given age = 65, classify the patient’s risk level:                               
    "High risk" if age > 60,
    "Moderate risk" if 40 ≤ age ≤ 60,
    "Low risk" otherwise.
    
    Returns:
        str: The patient risk classification.
    """
    age = 54
    if age > 60:
        return("High Risk")
    elif 40 <= age <= 60:
        return ("Moderate Risk")
    else:
        return("Low Risk")

print(patient_risk_level())



def image_resolution_classification():
    """
    Given resolution = "512x512", write an if-elif-else statement that classifies it as:
    "Low Resolution" if width < 512,
    "Medium Resolution" for 512 ≤ width ≤ 1024,
    "High Resolution" otherwise.
    
    Returns:
        str: The resolution classification.
    """
    resolution = "527x527"
    width = 527
    if width < 512:
        return "Low Resolution"
    elif 512<=width<=1024:
        return "Medium Resolution"
    else:
        return "High Resolution"
print(image_resolution_classification())


def determine_contrast_type():
    """
    Determine Contrast Type for MRI:
    If patient_age < 10, use "Pediatric contrast",
    If 10 ≤ patient_age < 60, use "Standard contrast",
    Otherwise, use "Low-dose contrast".
    
    Returns:
        str: The contrast type.
    """
    patient_age = 19
    if patient_age < 10:
        return "Pediatric Contrast"
    elif 10<=patient_age<= 10:
        return "Standard Contrast"
    else:
        return "Low-dose Contrast"
    
print(determine_contrast_type())


def scan_time_warning():
    """
    Given scan_time in minutes, print:
    "Fast scan" if time < 10,
    "Optimal scan" if 10 ≤ time ≤ 20,
    "Long scan, check settings" otherwise.
    
    Returns:
        str: The scan time classification.
    """
    scan_time = 32
    if scan_time < 10:
        return "Fast Scan"
    elif 10 <=scan_time<=20:
        return "Optimal Scan"
    else:
        return "Long scan, Check settings"
print(scan_time_warning())


def detect_motion_artifacts():
    """
    Given motion_level (ranging from 1 to 5), classify as:
    "Minimal artifact" if motion_level == 1,
    "Moderate artifact" if 2 ≤ motion_level ≤ 3,
    "Severe artifact, re-scan required" otherwise.
    
    Returns:
        str: The motion artifact classification.
    """
    motion_level = 4
    if motion_level == 1:
        return "Minimal artifact"
    elif 2<=motion_level<=3:
        return "Moderate artifact"
    else:
        return "Severe artifact, re-scan required"
    

print(detect_motion_artifacts())