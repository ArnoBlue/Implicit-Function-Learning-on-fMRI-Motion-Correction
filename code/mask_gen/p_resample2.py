

import nibabel as nib
import numpy as np
from scipy.ndimage import zoom
import os

def resample_image(img, new_spacing, order=1):
    """Resample image to new spacing."""
    # Get current spacing
    old_spacing = img.header.get_zooms()[:3]
    
    # Calculate the resize factor
    resize_factor = np.array(old_spacing) / np.array(new_spacing)
    
    # Perform resampling
    img_resampled = zoom(img.get_fdata(), resize_factor, order=order)
    
    # Create a new header with updated spacing
    new_header = img.header.copy()
    new_header.set_zooms(new_spacing)
    
    # Create a new Nifti1Image with the resampled data and updated header
    new_img = nib.Nifti1Image(img_resampled, img.affine, new_header)
    
    return new_img

def main(input_dir, output_dir):
    # Define new spacings and corresponding subdirectories
    spacings = {
        'xy_08mm_z_1mm': [0.8, 0.8, 1],
        'xz_08mm_y_1mm': [0.8, 1, 0.8],
        'yz_08mm_x_1mm': [1, 0.8, 0.8]
    }

    for key in spacings.keys():
        os.makedirs(os.path.join(output_dir, key), exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.nii.gz'):  # Process only NIfTI files
            input_filepath = os.path.join(input_dir, filename)
            original_img = nib.load(input_filepath)
            
            # Resample and save images
            for key, spacing in spacings.items():
                img_resampled = resample_image(original_img, spacing)
                
                new_filename = f"{os.path.splitext(filename)[0]}_{key}.nii.gz"
                output_filepath = os.path.join(output_dir, key, new_filename)

                nib.save(img_resampled, output_filepath)
                
                print(f"{key}:")
                print(f"File: {filename}")
                print(f"Dimensions: {img_resampled.shape}")
                print(f"Spacing: {img_resampled.header.get_zooms()}")
                print(f"Saved as: {output_filepath}\n")


if __name__ == '__main__':
    input_dir = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\feta\mask_ORI'
    output_dir = r'C:\Users\ausu\Desktop\CSP final project\Implicit Function Learning on fMRI Motion Correction\lab\in\A_final\A_final\feta\resample1_ORI'
    main(input_dir, output_dir)
