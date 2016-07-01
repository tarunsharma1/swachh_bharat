# 3D Reconstruction
We use VisualSFM for 3D reconstruction, additionally it uses many libraries for computation.

##Getting started:

    $ mkdir vsfm
    $ cd vsfm

##Setup NVIDIA CUDA

For SIFT matching and bundle adjustment we make use of GPU acceleration. CUDA-enabled NVIDIA GPUs is thus required.
It is also possible to set up out pipeline to use ATI/AMD GPUs via OpenCL, but it is for advanced users.

NVIDIA provides decent installation instructions (http://docs.nvidia.com/cuda/index.html).

Some tips for ubuntu users:
    
    Be sure to update your Ubuntu system before installation the CUDA software because if Ubuntu pushes you new Linux kernel, you’ll need to re-install the CUDA driver from scratch. 
    
    Install the driver first, then the toolkit.
    
    Reboot after installation.

To check if CUDA driver is working use the command:

    nvcc --version
    
This gives a response like:

    nvcc: NVIDIA (R) Cuda compiler driver
    Copyright (c) 2005-2015 NVIDIA Corporation
    Built on Tue_Aug_11_14:27:32_CDT_2015
    Cuda compilation tools, release 7.5, V7.5.17



