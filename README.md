# Implicit-Function-Learning-on-fMRI-Motion-Correction
In this work, an IFL-based SVR (IFLStVR) is achieved, which reconstructs an MRI volume of arbitrary resolution while correcting for the rigid motion of the slices. To improve the model's performance in the sharp portion of the volume, a new loss function is proposed to prevent extreme values. Meanwhile, a new mask generation method is introduced to control the output size accurately and simulate slices with different viewpoints. These slices can provide more information to the network making it more accurate output. Experiments are performed on adult brain fMRI, adult brain structural MRI, and fetal brain structural MRI. Experimental results show that IFLStVR can learn the implicit representation of MRI volume within 200 seconds. The proposed method performs well on adult and fetal structural MRI, with PSNR exceeding 30 and SSIM exceeding 0.88. For fMRI, the PSNR is improved by 3.2, and SSIM is improved by 0.7 compared to the baseline.


**Additional data mentioned for the poster presentation**

Experiments on the loss function:
<p align="center">
   <img src="./image/lamda.png" align="center" width="600">
</p>
<p align="center">Figure 1. Experimental results for different values of lambda.<p align="center">


Experimental results of different interpolation methods:
<p align="center">
   <img src="./image/interploation.png" align="center" width="600">
</p>
<p align="center">Figure 2. Experimental results of different interpolation methods.<p align="center">


Experimental results for minor and severe motions:
<p align="center">
   <img src="./image/minor.png" align="center" width="600">
</p>
<p align="center">Figure 3. Experimental results of minor motions.<p align="center">

<p align="center">
   <img src="./image/severe.png" align="center" width="600">
</p>
<p align="center">Figure 4. Experimental results of severe motions.<p align="center">


Motion simulation:
<p align="center">
   <img src="./image/motionf.png" align="center" width="600">
</p>
<p align="center">Figure 5. fMRI motion simulation.<p align="center">

<p align="center">
   <img src="./image/motions.png" align="center" width="600">
</p>
<p align="center">Figure 6. Adult structural MRI motion simulation..<p align="center">

<p align="center">
   <img src="./image/motionfe.png" align="center" width="600">
</p>
<p align="center">Figure 7. Fetal structural MRI motion simulation..<p align="center">


Optimal parameters for each type of data:
<p align="center">
   <img src="./image/best.png" align="center" width="600">
</p>
<p align="center">Figure 8. Optimal parameters for each type of data.<p align="center">

