import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Function to generate random dates
def random_date(start, end):
    return start + timedelta(days=np.random.randint(0, (end - start).days))

# Generate Patient Demographics Data
patients = pd.DataFrame({
    'Patient ID': range(1, 21),
    'Name': [f'Patient {i}' for i in range(1, 21)],
    'Age': np.random.randint(18, 90, size=20),
    'Gender': np.random.choice(['Male', 'Female'], size=20),
    'DoB': [random_date(datetime(1930, 1, 1), datetime(2005, 12, 31)).strftime('%Y-%m-%d') for _ in range(20)],
    'Mobile No': [f'+91{np.random.randint(6000000000, 9999999999)}' for _ in range(20)],
    'Email': [f'patient{i}@mail.com' for i in range(1, 21)],
    'Address': [f'Address {i}' for i in range(1, 21)],
    'Insurance Provider': np.random.choice(['Provider A', 'Provider B', 'Provider C'], size=20),
    'Emergency Contact Name': [f'EC {i}' for i in range(1, 21)],
    'Emergency Contact Mobile No.': [f'+91{np.random.randint(6000000000, 9999999999)}' for _ in range(20)],
    'Blood Type': np.random.choice(['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-'], size=20),
    'Allergies': np.random.choice(['None', 'Peanuts', 'Dust', 'Pollen', 'Milk'], size=20)
})

# Generate Basic Medical Details Data
basic_medical = pd.DataFrame({
    'Patient ID': patients['Patient ID'],
    'Height (cms)': np.random.randint(150, 200, size=20),
    'Weight (kg)': np.random.randint(50, 120, size=20),
    'BMI': np.round(np.random.uniform(18.5, 35, size=20), 2),
    'Smoking status': np.random.choice(['Never', 'Former', 'Light', 'Heavy'], size=20),
    'Drinking status': np.random.choice(['Never', 'Former', 'Light', 'Heavy'], size=20),
    'Exercise frequency': np.random.choice(['Inactive', 'Light', 'Heavy'], size=20),
    'Dietary Habits': np.random.choice(['Veg', 'Non-veg', 'Vegan'], size=20),
    'Personal History': np.random.choice(['None', 'Urinary Problems', 'Bowel Problems', 'Addictions'], size=20)
})

# Generate Medical History Data
medical_history = pd.DataFrame({
    'Patient ID': patients['Patient ID'],
    'Conditions': np.random.choice(['None', 'Hypertension', 'Diabetes', 'Asthma'], size=20),
    'Diagnosis Date': [random_date(datetime(2010, 1, 1), datetime(2024, 1, 1)).strftime('%Y-%m-%d') for _ in range(20)],
    'Status': np.random.choice(['Ongoing', 'Resolved'], size=20),
    'Medical drug history': np.random.choice(['None', 'Antibiotics', 'Painkillers'], size=20),
    'Past History': np.random.choice(['None', 'Hypertension', 'Heart Disease'], size=20),
    'Family History': np.random.choice(['None', 'Cancer', 'Diabetes'], size=20),
    'Menstrual History': np.random.choice(['None', 'Regular', 'Irregular'], size=20),
    'Obstetric History': np.random.choice(['None', '1 child', '2 children'], size=20)
})

# Generate Medications Data
medications = pd.DataFrame({
    'Patient ID': patients['Patient ID'],
    'Medication': np.random.choice(['Paracetamol', 'Ibuprofen', 'None'], size=20),
    'Dosage': np.random.choice(['500mg', '250mg', 'None'], size=20),
    'Frequency': np.random.choice(['Once a day', 'Twice a day', 'None'], size=20),
    'Start Date': [random_date(datetime(2020, 1, 1), datetime(2024, 1, 1)).strftime('%Y-%m-%d') for _ in range(20)],
    'End Date': [random_date(datetime(2024, 1, 2), datetime(2025, 1, 1)).strftime('%Y-%m-%d') for _ in range(20)]
})

# Print Sample Data
print("Patient Demographics:")
print(patients.head())
print("\nBasic Medical Details:")
print(basic_medical.head())
print("\nMedical History:")
print(medical_history.head())
print("\nMedications:")
print(medications.head())
