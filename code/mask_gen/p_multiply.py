

import nibabel as nib
import numpy as np
import os


folder1_path = r'E:\desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\fmri\mask_ORI_trans_resample0\yz_1mm_x_3mm'
folder2_path = r'E:\desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\fmri\ORI_trans_resample1\yz_1mm_x_3mm'
output_folder_path = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\fmri\multiply_input\no_motion'


os.makedirs(output_folder_path, exist_ok=True)

files1 = sorted(os.listdir(folder1_path))
files2 = sorted(os.listdir(folder2_path))


for file1, file2 in zip(files1, files2):
    file1_path = os.path.join(folder1_path, file1)
    file2_path = os.path.join(folder2_path, file2)

    mri1 = nib.load(file1_path)
    mri2 = nib.load(file2_path)

    data1 = mri1.get_fdata()
    data2 = mri2.get_fdata()

    result_data = data1 * data2

    # Create a new NIfTI image using the header and affine matrices of file 1
    new_img = nib.Nifti1Image(result_data, affine=mri1.affine, header=mri1.header)


    output_file_path = os.path.join(output_folder_path, file1)
    nib.save(new_img, output_file_path)


    print(f"Processing completed: {file1} 和 {file2}")

