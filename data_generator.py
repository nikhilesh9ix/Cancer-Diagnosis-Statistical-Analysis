"""
Synthetic Medical Data Generator for Cancer Diagnosis
Generates realistic medical data with tumor characteristics and patient demographics.
"""

import pandas as pd
import numpy as np
from typing import Tuple
import os

def generate_medical_data(n_samples: int = 1000, random_state: int = 42) -> pd.DataFrame:
    """
    Generate synthetic medical data for cancer diagnosis research.
    
    Parameters:
    -----------
    n_samples : int
        Number of samples to generate (default: 1000)
    random_state : int
        Random seed for reproducibility (default: 42)
    
    Returns:
    --------
    pd.DataFrame
        Synthetic medical dataset with tumor characteristics
    """
    np.random.seed(random_state)
    
    # Generate diagnosis first (30% malignant, 70% benign - realistic distribution)
    diagnosis = np.random.choice(['Benign', 'Malignant'], size=n_samples, p=[0.7, 0.3])
    
    # Initialize arrays for features
    tumor_size = np.zeros(n_samples)
    smoothness = np.zeros(n_samples)
    compactness = np.zeros(n_samples)
    patient_age = np.zeros(n_samples)
    
    for i in range(n_samples):
        if diagnosis[i] == 'Malignant':
            # Malignant tumors tend to be larger, less smooth, more compact
            tumor_size[i] = np.random.normal(15.0, 4.0)  # Mean 15mm, larger
            smoothness[i] = np.random.normal(0.08, 0.02)  # Lower smoothness (more irregular)
            compactness[i] = np.random.normal(0.12, 0.03)  # Higher compactness
            patient_age[i] = np.random.normal(58, 12)  # Slightly older on average
        else:
            # Benign tumors tend to be smaller, smoother, less compact
            tumor_size[i] = np.random.normal(10.0, 3.0)  # Mean 10mm, smaller
            smoothness[i] = np.random.normal(0.10, 0.015)  # Higher smoothness (more regular)
            compactness[i] = np.random.normal(0.08, 0.02)  # Lower compactness
            patient_age[i] = np.random.normal(52, 15)  # Slightly younger on average
    
    # Ensure realistic ranges
    tumor_size = np.clip(tumor_size, 2.0, 30.0)  # 2-30mm range
    smoothness = np.clip(smoothness, 0.02, 0.20)  # 0.02-0.20 range
    compactness = np.clip(compactness, 0.01, 0.30)  # 0.01-0.30 range
    patient_age = np.clip(patient_age, 18, 90)  # 18-90 years range
    
    # Create DataFrame
    data = pd.DataFrame({
        'Patient_ID': [f'P{str(i+1).zfill(4)}' for i in range(n_samples)],
        'Tumor_Size': np.round(tumor_size, 2),
        'Smoothness': np.round(smoothness, 4),
        'Compactness': np.round(compactness, 4),
        'Patient_Age': np.round(patient_age, 0).astype(int),
        'Diagnosis': diagnosis
    })
    
    return data

def save_dataset(data: pd.DataFrame, filename: str = 'cancer_diagnosis_data.csv') -> str:
    """
    Save the generated dataset to a CSV file.
    
    Parameters:
    -----------
    data : pd.DataFrame
        The dataset to save
    filename : str
        Name of the output file
    
    Returns:
    --------
    str
        Path to the saved file
    """
    filepath = os.path.join(os.path.dirname(__file__), filename)
    data.to_csv(filepath, index=False)
    return filepath

def main():
    """Generate and save the synthetic medical dataset."""
    print("Generating synthetic medical data for cancer diagnosis...")
    
    # Generate dataset
    data = generate_medical_data(n_samples=1000, random_state=42)
    
    # Save to CSV
    filepath = save_dataset(data)
    
    # Display basic information
    print(f"Dataset generated and saved to: {filepath}")
    print(f"Dataset shape: {data.shape}")
    print("\nDataset preview:")
    print(data.head(10))
    print("\nDiagnosis distribution:")
    print(data['Diagnosis'].value_counts())
    print("\nBasic statistics:")
    print(data.describe())

if __name__ == "__main__":
    main()