import numpy as np
import h5py
import pickle
import cv2
import math

a=pickle.load(open('./bounding_box_val_data.npy','r'))
k=0
for i in a.keys():
	img = i
	values = a[i]
	img = cv2.imread(img)
	img = cv2.resize(img,(227,227),interpolation=cv2.INTER_CUBIC)

	b=img[:,:,0]
        g=img[:,:,1]
        r=img[:,:,2]

        img3=np.zeros((3,227,227),dtype=np.uint8)

        img3[0]=b
        img3[1]=g
        img3[2]=r


	img3 = img3[np.newaxis,...]

	print values
	for j in range(0,4):
		if(values[j]<0):
			values[j]=0
		values[j] = math.log(values[j]+1)

	values = np.array(values)
	values=values[np.newaxis,...]
        values=values[np.newaxis,...]
        values=values[np.newaxis,...]

	output = h5py.File('./hdf5_dataset/val'+str(k)+'.h5','w')
        output.create_dataset('image', data=img3)
	output.create_dataset('values',data=values)
        output.close()
        
	k=k+1	

	print img3.shape, values.shape
	#exit(0)


