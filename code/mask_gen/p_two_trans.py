

import os
import numpy as np
import nibabel as nib
from scipy.ndimage import affine_transform

def generate_random_rigid_transform():

    angle = np.random.uniform(-5, 5)  
    rotation_matrix = np.array([
        [np.cos(np.radians(angle)), -np.sin(np.radians(angle)), 0],
        [np.sin(np.radians(angle)), np.cos(np.radians(angle)), 0],
        [0, 0, 1]
    ])
    
    translation_vector = np.random.uniform(-5, 5, size=3)  # random translation vector
    
    transform_matrix = np.eye(4)
    transform_matrix[:3, :3] = rotation_matrix
    transform_matrix[:3, 3] = translation_vector
    
    return transform_matrix

def apply_transform_to_slice(mri_data, transform_matrix, slice_index):

    mri_data[..., slice_index] = affine_transform(mri_data[..., slice_index], transform_matrix[:3, :3], offset=transform_matrix[:3, 3], order=0)
    return mri_data

def process_mri_files(input_dir_1, input_dir_2, output_dir_1, output_dir_2):

    os.makedirs(output_dir_1, exist_ok=True)
    os.makedirs(output_dir_2, exist_ok=True)
    
    files_1 = sorted(os.listdir(input_dir_1))
    files_2 = sorted(os.listdir(input_dir_2))
    
    for file_1, file_2 in zip(files_1, files_2):
        input_path_1 = os.path.join(input_dir_1, file_1)
        input_path_2 = os.path.join(input_dir_2, file_2)
        output_path_1 = os.path.join(output_dir_1, file_1)
        output_path_2 = os.path.join(output_dir_2, file_2)
        
        print(f'Processing files: {file_1} and {file_2}')
        
        img1 = nib.load(input_path_1)
        img2 = nib.load(input_path_2)
        
        data1 = img1.get_fdata()
        data2 = img2.get_fdata()
        
        for i in range(0, data1.shape[2], 3):
            transform_matrix = generate_random_rigid_transform()
            
            data1 = apply_transform_to_slice(data1, transform_matrix, i)
            data2 = apply_transform_to_slice(data2, transform_matrix, i)
        
        new_img1 = nib.Nifti1Image(data1, img1.affine)
        new_img2 = nib.Nifti1Image(data2, img2.affine)
        
        nib.save(new_img1, output_path_1)
        nib.save(new_img2, output_path_2)


input_dir_1 = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\feta\mask_ORI'
input_dir_2 = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\feta\ORI'
output_dir_1 = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\feta\mask_ORI_trans5'
output_dir_2 = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\feta\ORI_trans5'


process_mri_files(input_dir_1, input_dir_2, output_dir_1, output_dir_2)
