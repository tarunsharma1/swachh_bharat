import numpy as np
import cv2
import pickle
import sys
import os
import glob
#sys.path.insert(0,'C:/Users/tarun_000/Desktop/mad_street_den/ml_shiz/gdbn/gdbn/')
import gnumpy as gnp
sys.path.insert(0,'/home/tarun/gdbn')
import gdbn
from gdbn.dbn import * 
import sys

global number,net_layers

def area(a,b):
    dx=min(a[2],b[2]) - max(a[0],b[0])
    dy=min(a[3],b[3]) - max(a[1],b[1])
    if(dx>=0 and dy>=0):
        return dx*dy
    else:
        return 0    

def classifier_init():
    global net_layers

    weights = open('./weights_bounding_box.npy','rb')
    weights = pickle.load(weights)

    biases = open('./biases_bounding_box.npy','rb')
    biases = pickle.load(biases)

    layerSizes = [1024,512, 4]
    scales = [0.05 for i in range(len(layerSizes)-1)]
    fanOuts = [None for i in range(len(layerSizes)-1)]

    net_layers = buildDBN(layerSizes, scales, fanOuts, Linear(), True,True)
    net_layers.weights = weights
    net_layers.biases = biases


classifier_init()

#f=open('./bounding_box_val_data.npy','rb')
#p=pickle.load(f)
main_count = 0


testInps=np.zeros((1,1024),dtype=num.float32)
#path ='/home/tarun/ccbd/ccbd_images/bounding_box_val/*.jpg' 
path = '/home/tarun/ccbd/ccbd_images/pallavi/*.jpg'  
files=glob.glob(path)
for file2 in files:
    img=cv2.imread(file2,0)
    img = cv2.resize(img,(32,32),interpolation=cv2.INTER_CUBIC)
    img = np.reshape(img[0:32,0:32],(1,1024))
    testInps[0,:] = img/255.0

    #print 'actual values :',trainTargs[50,:]
    #print 'predicted values:',net_layers.fprop(testInps[0,:])*500.0

    output = net_layers.fprop(testInps[0,:])*500.0
    startx = abs(int(output[0][0]))

    starty = abs(int(output[0][1]))
    w = abs(int(output[0][2]))
    h = abs(int(output[0][3]))
    #print file2

    pic = cv2.imread(file2)
    pic = cv2.resize(pic,(500,500),interpolation=cv2.INTER_CUBIC)
    pic2 = pic[starty:starty+h,startx:startx+w]
    #pic2 = cv2.resize(pic2,(350,350),interpolation=cv2.INTER_CUBIC)
    cv2.rectangle(pic, (startx, starty),(startx+w,starty+h), (0, 255, 0), 2)
    cv2.imshow('window',pic)
    cv2.waitKey(0)
    #cv2.imwrite('./ccbd_images/Vivek_segmented/pallavi/'+file2.split('/')[-1],pic2)
    #cv2.waitKey(0)
    # pr = [startx,starty,w,h]
    # gt = p[file2]
    # unionCoords = [min(gt[0],pr[0]),min(gt[1],pr[1]),max(gt[0]+gt[2]-1,pr[0]+pr[2]-1),max(gt[1]+gt[3]-1,pr[1]+pr[3]-1)]
    # unionArea=(unionCoords[2]-unionCoords[0]+1)*(unionCoords[3]-unionCoords[1]+1)
    # ra = [gt[0],gt[1],gt[0]+gt[2],gt[1]+gt[3]]
    # rb = [pr[0],pr[1],pr[0]+pr[2],pr[1]+pr[3]]
    # intersectionArea = area(ra,rb)
    # if(intersectionArea/float(unionArea) > 0.5):
    #     main_count = main_count + 1
    #     print file2

print main_count