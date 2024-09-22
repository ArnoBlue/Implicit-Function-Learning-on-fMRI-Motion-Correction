

import nibabel as nib
import numpy as np
import os

folder_path = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\feta\ORI'

for filename in os.listdir(folder_path):
    if filename.endswith('.nii') or filename.endswith('.nii.gz'):  # 仅处理NIfTI文件
        file_path = os.path.join(folder_path, filename)
        
       
        mri_img = nib.load(file_path)
   
        mri_data = mri_img.get_fdata()
        
        # Filter out 0 values and calculate the mean
        non_zero_values = mri_data[mri_data != 0]
        mean_value = np.mean(non_zero_values)
        
        # Print the file name and mean value
        print(f'file: {filename}, The mean of all values except 0 is: {mean_value}')
