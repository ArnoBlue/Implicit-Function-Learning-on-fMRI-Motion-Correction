
import nibabel as nib
import numpy as np
import os

def modify_affine(input_path, output_path, new_affine):

    img = nib.load(input_path)
    
    # Getting the raw data and header
    data = img.get_fdata()
    header = img.header
    
    new_img = nib.Nifti1Image(data, affine=new_affine, header=header)

    nib.save(new_img, output_path)
    
    print(f"New MRI data saved to {output_path} with updated affine matrix.")

def batch_modify_affine(directory_path, new_affine):

    for filename in os.listdir(directory_path):
        if filename.endswith(".nii.gz"):
            input_file_path = os.path.join(directory_path, filename)
            output_file_path = os.path.join(directory_path, f"aff_{filename}")
            

            modify_affine(input_file_path, output_file_path, new_affine)

directory_path = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\fmri\mask_ORI_trans'
new_affine_matrix = np.array([[-3.0, 0.0, 0.0, 90.0], 
                              [0.0, 1.0, 0.0, -126.0], 
                              [0.0, 0.0, 1.0, -72.0], 
                              [0.0, 0.0, 0.0, 1.0]])

batch_modify_affine(directory_path, new_affine_matrix)
