#!/bin/bash 

# This script needs SiftGPU for feature detection and matching, 
# PBA for sparse reconstruction, 
# PMVS/CMVS for dense reconstruction.
# ----------------------------------------------------------------------------------------------------------

# Run VisualSFM help 


# VisualSFM sfm[options] input output.nvm [user_data_path]
#     options = [match_option][sfm_option][misc_option][mvs_option]
#     match_option = [+pairs/+import/+subset/+nomatch/]
#         +pairs:   match image pairs from [user_data_path];
#         +import:  load feature matches from [user_data_path];
#         +subset:  match a prioritized subset of pairs when
#                   #images >= param_prioritized_subset_switch;
#         +nomatch: reconstruction without feature matching;
#         default:  compute missing pairwise matches.
#     sfm_option = [+resume/+add/+skipsfm/+loadnvm/]
#         +resume:  load NVM file, try add new images from
#                   [input].txt, and grow the existing models;
#         +add:     load NVM file, and find more points and
#                   projections for the existing models;
#         +loadnvm: load NVM file and skip feature matching;
#         +skipsfm: skip sparse and dense reconstruction;
#         default:  run regular sparse reconstruction.
#     misc_option = [+k=fx,cx,fy,cy/+shared][+sort][+gcp]
#         +k:       fixed calibration, e.g. +k=1024,800,1024,600;
#         +shared:  enforce shared calibration in the end;
#         +sort:    keep the input image order in the output NVM;
#         +gcp:     load GCPs from [input].gcp and transform the 3D model.
#     mvs_option = [+pmvs/+cmvs/+cmp/]
#         +cmvs:    undistort images, run CMVS/genOption, skip PMVS;
#         +pmvs:    undistort images, run CMVS/genOption/PMVS;
#         +cmp:     undistort images, write p-matrices for CMP-MVS;
#         default:  skip the entire dense reconstruction.
#     <output.nvm> is where reconstruction is saved.
#        You can open it afterwards for visualization.
# -------------------------------------------------------------------------------------------------------------

# inputImageFolder - Represents the location of segmented images.
#				   - This is the result of segmentation step.
#				   - Be sure to make seperate folders for test sets

inputImageFolder= "/home/susheel/Documents/ccbd/vsfm/testImages/segmentedGarbage" 

# as an example here segmentedGarbage ins folder which contains 8 segmented images.

# outputPlyFolder - Represents location of generated nvm and ply files.
# 				  - This can later be used in volume estimation.
                  

outputPlyFolder = "/home/susheel/Documents/ccbd/vsfm/results/segmentedGarbage/output.nvm" 

VisualSFM sfm+pmvs+cmvs $inputImageFolder $outputPlyFolder 