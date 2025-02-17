import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Function to generate random dates
def random_date(start, end, size):
    return [start + timedelta(days=random.randint(0, (end - start).days)) for _ in range(size)]

# Number of patients
num_patients = 50000  # Increased from 10,000 to 50,000

# Sample patient data
patients = pd.DataFrame({
    "Patient ID": [f"P{i+1}" for i in range(num_patients)],
    "Name": [f"Patient {i+1}" for i in range(num_patients)],
    "Age": np.random.randint(20, 80, size=num_patients),
    "Gender": np.random.choice(["Male", "Female"], size=num_patients),
    "DoB": random_date(datetime(1940, 1, 1), datetime(2005, 12, 31), num_patients),
    "Mobile No": [f"987654{random.randint(1000,9999)}" for _ in range(num_patients)],
    "Email": [f"patient{i+1}@example.com" for i in range(num_patients)],
    "Address": ["Address " + str(i+1) for i in range(num_patients)],
    "Insurance Provider": np.random.choice(["Aetna", "Blue Cross", "United Healthcare", "None"], size=num_patients),
    "Emergency Contact Name": [f"Guardian {i+1}" for i in range(num_patients)],
    "Emergency Contact Mobile No.": [f"912345{random.randint(1000,9999)}" for _ in range(num_patients)],
    "Blood Type": np.random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], size=num_patients),
    "Allergies": np.random.choice(["None", "Penicillin", "Pollen", "Nuts", "Dust"], size=num_patients)
})

# Sample Basic Medical Details
basic_medical = pd.DataFrame({
    "Patient ID": patients["Patient ID"],
    "Height (cms)": np.random.randint(150, 200, size=num_patients),
    "Weight (kg)": np.random.randint(50, 100, size=num_patients),
    "BMI": np.random.uniform(18.5, 30, size=num_patients).round(2),
    "Smoking status": np.random.choice(["Never", "Former", "Light", "Heavy"], size=num_patients),
    "Drinking status": np.random.choice(["Never", "Former", "Light", "Heavy"], size=num_patients),
    "Exercise frequency": np.random.choice(["Inactive", "Light", "Heavy"], size=num_patients),
    "Dietary Habits": np.random.choice(["Veg", "Non-veg", "Vegan"], size=num_patients),
    "Personal History": np.random.choice(["None", "Bowel problems", "Addictions", "Urinary problems"], size=num_patients)
})

# Sample Medical History
diagnosis_status = ["Active", "Recovered", "Chronic"]
medical_history = pd.DataFrame({
    "Patient ID": patients["Patient ID"],
    "Conditions": np.random.choice(["Hypertension", "Diabetes", "Asthma", "None"], size=num_patients),
    "Diagnosis Date": random_date(datetime(2010, 1, 1), datetime(2024, 1, 1), num_patients),
    "Status": np.random.choice(diagnosis_status, size=num_patients),
    "Medical drug history and allergy": np.random.choice(["None", "Penicillin", "Sulfa Drugs"], size=num_patients),
    "Past History": np.random.choice(["Hypertension", "Diabetes", "Asthma", "None"], size=num_patients),
    "Family History": np.random.choice(["None", "Cancer", "Heart Disease"], size=num_patients)
})

# Sample Appointments
appointments = pd.DataFrame({
    "Patient ID": patients["Patient ID"],
    "Appointment No.": [f"A{i+1}" for i in range(num_patients)],
    "Doctor's Name": np.random.choice(["Dr. Smith", "Dr. Johnson", "Dr. Lee"], size=num_patients),
    "Date": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1), num_patients),
    "Reason": np.random.choice(["Routine Checkup", "Follow-up", "Emergency Visit"], size=num_patients)
})

# Sample Medications
medications = pd.DataFrame({
    "Patient ID": patients["Patient ID"],
    "Medication": np.random.choice(["Paracetamol", "Insulin", "Aspirin", "None"], size=num_patients),
    "Dosage": np.random.choice(["Once a day", "Twice a day", "Weekly"], size=num_patients),
    "Frequency": np.random.choice(["Daily", "As needed"], size=num_patients),
    "Start Date": random_date(datetime(2020, 1, 1), datetime(2024, 1, 1), num_patients),
    "End Date": random_date(datetime(2024, 2, 1), datetime(2025, 12, 31), num_patients)
})

# Sample Lab Test Results
lab_tests = pd.DataFrame({
    "Patient ID": patients["Patient ID"],
    "Test Name": np.random.choice(["Blood Test", "X-Ray", "MRI", "CT Scan"], size=num_patients),
    "Result": np.random.choice(["Normal", "Abnormal"], size=num_patients),
    "Date": random_date(datetime(2022, 1, 1), datetime(2024, 1, 1), num_patients),
    "Normal Range": ["Varies" for _ in range(num_patients)]
})

# Exporting to CSV
patients.to_csv("patients.csv", index=False)
basic_medical.to_csv("basic_medical.csv", index=False)
medical_history.to_csv("medical_history.csv", index=False)
appointments.to_csv("appointments.csv", index=False)
medications.to_csv("medications.csv", index=False)
lab_tests.to_csv("lab_tests.csv", index=False)

print("CSV files for all tables with 50,000 records created successfully!")
