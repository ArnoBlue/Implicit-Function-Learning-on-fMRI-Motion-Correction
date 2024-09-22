

import os
import nibabel as nib
import numpy as np

def create_mask_from_mri(input_filename, output_filename):
    # Reading MRI files
    mri_img = nib.load(input_filename)
    mri_data = mri_img.get_fdata()
    
    # Creating a Mask
    mask_data = np.where(mri_data != 0, 1, 0)
    
    # Creating NIfTI images
    mask_img = nib.Nifti1Image(mask_data, mri_img.affine, mri_img.header)
    
    # Save mask file
    nib.save(mask_img, output_filename)

def process_mri_folder(input_folder, output_folder):
    # Make sure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through all .nii.gz files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.nii.gz'):
            input_filepath = os.path.join(input_folder, filename)
            output_filename = f"mask_{filename}"
            output_filepath = os.path.join(output_folder, output_filename)
            
            # Create a mask and save it
            create_mask_from_mri(input_filepath, output_filepath)
            print(f"Processed {filename} and saved mask as {output_filename}")

input_folder = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\feta\ORI'
output_folder = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\feta\mask_ORI'
process_mri_folder(input_folder, output_folder)


