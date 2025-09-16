import nibabel as nib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from nilearn import image, masking
import os

def load_nifti(file_path):
    """Load a NIfTI file and return the image data as a numpy array."""
    img = nib.load(file_path)
    data = img.get_fdata()
    return data

if __name__ == "__main__":
    data_path = "F:\data\NEURAL_DATA"
    subjects = os.listdir(data_path)
    print(subjects)