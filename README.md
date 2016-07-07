# swachh_bharat
There are 3 folders:
	segmentation,
	3DReconstruction,
	volumeEstimation
volumeEstimation:
Inside this folder is the MLX script to subsample and Mesh the point clouds obtained from the 3d sfm ( structure from motion approach ). This would be the last step of the pipeline. 
Step 1: segmentation.-> Step 2:. 3d SFM.-> Step 3: Meshing and Volume estimation

Once the script is executed on Meshlab, you must apply the Filter called "Compute Geometric Measures". There is enough documentation online for Meshlab to help you apply the script inside it.
Once you have computed the geometry, you will obtain a bunch of values in the console. ( The console is visible if you click the "Layers"option on the toolbar). In these values, take out only the bounding box values. They will be 3 space separated values for length, breadth and height. Multiply it to get the boundary box volume and multiply it with 0.229 to get volume in metric units.


Some useful links: https://www.youtube.com/watch?v=UQsg3-WOj9E
https://vimeo.com/20933872, http://www.andrewhazelden.com/blog/2012/04/automate-your-meshlab-workflow-with-mlx-filter-scripts/
