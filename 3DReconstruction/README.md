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

1. Be sure to update your Ubuntu system before installation the CUDA software because if Ubuntu pushes you new Linux kernel, you’ll need to re-install the CUDA driver from scratch. 

2. Install the driver first, then the toolkit.

3. Reboot after installation.

To check if CUDA driver is working use the command:

    nvcc --version
    
This gives a response like:

    nvcc: NVIDIA (R) Cuda compiler driver
    Copyright (c) 2005-2015 NVIDIA Corporation
    Built on Tue_Aug_11_14:27:32_CDT_2015
    Cuda compilation tools, release 7.5, V7.5.17

##Download the Necessary Libraries:

1. VisualSFM (available as a zip in this repository)
2. SiftGPU (available from http://www.cs.unc.edu/~ccwu/siftgpu/)
3. Multicore Bundle Adjustment (available from http://grail.cs.washington.edu/projects/mcba/)
4. PMVS-2 (available from http://www.di.ens.fr/pmvs/documentation.html)
5. CMVS (available from http://www.di.ens.fr/cmvs/documentation.html)
6. Graclus 1.2 (http://www.cs.utexas.edu/users/dml/Software/graclus.html it contains a form that asks for an email address prior to download)

##Install Dependency Packages:

    $ sudo apt-get install libgtk2.0-dev libglew1.6-dev libglew1.6 libdevil-dev libboost-all-dev libatlas-cpp-0.6-dev libatlas-dev imagemagick libatlas3gf-base libcminpack-dev libgfortran3 libmetis-edf-dev libparmetis-dev freeglut3-dev libgsl0-dev 

##Build VisualSFM:

    $ unzip VisualSFM_linux_64bit.zip 
    $ cd vsfm 
    $ make
    
##Build SiftGPU:

    $ unzip SiftGPU-V382.zip 
    $ cd SiftGPU
    $ make
    $ cp bin/libsiftgpu.so ../vsfm/bin

##Build Multicore Bundle Adjustment (a.k.a. “pba”):
Thiis is a tricky part. Unzip (“unzip pba_v1.0.4.zip”), and then you’ll need to edit two source code files. In “pba/src/pba”, edit “SparseBundleCU.h” and “pba.h” by adding this one line to the top of each file:

    #include <stdlib.h>

Now you can compile if you simply type “make” in the “~/vsfm/pba” directory.


##Build PMVS-2:

    $ tar xf pmvs-2.tar.gz
    $ cd pmvs-2/program/main/
    $ cp mylapack.o mylapack.o.backup
    $ make clean
    $ cp mylapack.o.backup mylapack.o
    $ make depend
    $ make

##Build Graclus 1.2:
    
After you untar graclus1.2.tar.gz, you do need to edit “Makefile.in” to set “-DNUMBITS=64″ so that the library works with your 64-bit VisualSFM installation. After making that change to the makefile, just type “make”, and it should work.

##Build CMVS:

OK, now the hard part. First, unzip CMVS and grab that mylapack.o file from the PMVS-2 binary distribution:

    $ cd ~/vsfm
    $ tar xf cmvs-fix2.tar.gz
    $ cp pmvs-2/program/main/mylapack.o cmvs/program/main/

Next, edit the source file “cmvs/program/base/cmvs/bundle.cc” by adding these includes at the top of the file:

    #include <vector>
    #include <numeric>

And now edit “cmvs/program/main/genOption.cc” by adding this include statement at the top:

    #include <stdlib.h>
    
##OK, almost there! 

Now edit the CMVS Makefile (in cmvs/program/main) so that lines 10-17 read as follows (but be sure to replace “/home/susheel/Documents/ccbd/vsfm/” with the path to your installation):

    #Your INCLUDE path (e.g., -I/usr/include)
    YOUR_INCLUDE_PATH =

    #Your metis directory (contains header files under graclus1.2/metisLib/)
    YOUR_INCLUDE_METIS_PATH = -I/home/susheel/Documents/ccbd/vsfm/graclus1.2/metisLib

    #Your LDLIBRARY path (e.g., -L/usr/lib)
    YOUR_LDLIB_PATH = -L//home/susheel/Documents/ccbd/vsfm/graclus1.2

OK, now go ahead and build the thing, and then copy the three binaries into the VisualSFM binary directory.

    $ cd ~/vsfm/cmvs/program/main
    $ make
    $ cp cmvs ~/vsfm/vsfm/bin
    $ cp pmvs2 ~/vsfm/vsfm/bin
    $ cp genOption ~/vsfm/vsfm/bin

##Running VisualSFM

Finally, add VisualSFM to your path and LD_LIBRARY_PATH. You can do this by adding lines to your ~/.bashrc file. Here’s what I added to the bottom of mine: (please change according to your installation path)

    export PATH=$PATH:/home/susheel/Documents/ccbd/vsfm/vsfm/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/susheel/Documents/ccbd/vsfm/vsfm/bin

##Running the script for 3D Reconstruction











    




