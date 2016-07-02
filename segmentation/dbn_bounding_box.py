import sys
sys.path.insert(0,'/home/tarun/gdbn')
import numpy as num
import itertools
from gdbn.dbn import *
import matplotlib.pyplot as plt
import cv2
import time

def numMistakes(targetsMB, outputs):
    if not isinstance(outputs, num.ndarray):
        outputs = outputs.as_numpy_array()
    if not isinstance(targetsMB, num.ndarray):
        targetsMB = targetsMB.as_numpy_array()
    return num.sum(outputs.argmax(1) != targetsMB.argmax(1))

def sampleMinibatch(mbsz, inps, targs):
    idx = num.random.randint(inps.shape[0], size=(mbsz,))
    return inps[idx], targs[idx]


import numpy as np
trainInps=np.zeros((313,1024),dtype=num.float32)
trainTargs=np.zeros((313,4),dtype=num.float32)


testInps=np.zeros((460,1024),dtype=num.float32)
testTargs=np.zeros((460,2),dtype=num.float32)

mbsz = 64
layerSizes = [1024,512,4]
scales = [0.05 for i in range(len(layerSizes)-1)]
fanOuts = [None for i in range(len(layerSizes)-1)]
learnRate = 0.01
epochs = 2000
mbPerEpoch = int(num.ceil(313./mbsz))

import pickle
f=open('./bounding_box_training_data.npy','rb')
p=pickle.load(f)
data=p

i=0
for key in data.keys():
    img=cv2.imread(key,0)
    img = cv2.resize(img,(32,32),interpolation=cv2.INTER_CUBIC)
    img = np.reshape(img[0:32,0:32],(1,1024))
    if(data[key][2]!=0 and data[key][3]!=0):
        trainInps[i,:]=img
        trainTargs[i,:]=data[key]
        i=i+1
    #print img.shape

print 'reading done'
print i

# f=open('./training_labels.npy','rb')
# p=pickle.load(f)
# labels=p

#normalize it
for i in range(0,313):
    trainInps[i,:]=trainInps[i,:]/255.0

for i in range(0,313):
    trainTargs[i,:]=trainTargs[i,:]/500.0
# trainInps = data
# trainTargs = labels


# f=open('./testing_data.npy','rb')
# p=pickle.load(f)
# data=p

# f=open('./testing_labels.npy','rb')
# p=pickle.load(f)
# labels=p

# #normalize it
# for i in range(0,460):
#     data[i][:]=data[i][:]/255.0

# testInps = data
# testTargs = labels

mbStream = (sampleMinibatch(mbsz, trainInps, trainTargs) for unused in itertools.repeat(None))

   
scales = [0.1 for i in range(len(layerSizes)-1)]
fanOuts = [None for i in range(len(layerSizes)-1)]
dropOuts = [0.25 for i in range(len(layerSizes)-1)]

net = buildDBN(layerSizes, scales, fanOuts, Linear(), True,True)
net.learnRates = [learnRate for x in net.learnRates]
net.L2Costs = [0 for x in net.L2Costs]
net.nestCompare = True #this flag existing is a design flaw that I might address later, for now always set it to True


#print net.fprop(trainInps[i,:])

for ep, (trCE, trEr) in enumerate(net.fineTune(mbStream,epochs, mbPerEpoch, numMistakes,True)):
    print ep, trCE, trEr
    #print 'OUTPUT AFTER:',net.fprop(trainInps[0,:])
    #time.sleep(10)

print net.fprop(trainInps[100,:])
#outputs = tuple(net.predictions(testInps))
# outputs = num.array(outputs).reshape(testInps.shape[0], -1)


print '##### TESTING ##########'
print 'actual values :',trainTargs[50,:]*500.0
print 'predicted values:',net.fprop(trainInps[50,:])*500.0

# print "Test error rate:", numMistakes(
#     testTargs, outputs) / float(testInps.shape[0])
savedWeights = net.weights
savedBiases = net.biases

pickle.dump( savedWeights, open( "weights_bounding_box.npy", "wb" ) )
pickle.dump( savedBiases, open( "biases_bounding_box.npy", "wb" ) )



#np.savez('weights',data=savedWeights)
#np.savez('biases',data=savedBiases)

