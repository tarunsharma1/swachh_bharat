import cv2
import os
import glob
import pickle

# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)

def click_and_crop(event,x,y,flags,params):
	global startx,starty,endx,endy
	global w,h
	global pic
	if event == cv2.EVENT_LBUTTONDOWN:
		#store starting coordinates
		startx = x
		starty = y
	elif event == cv2.EVENT_LBUTTONUP:
		endx = x
		endy = y
		w=	endx - startx
		h= 	endy - starty	
		#print startx, starty,w,h
		cv2.rectangle(pic, (startx, starty),(endx,endy), (0, 255, 0), 2)
		#cv2.imshow('window',pic)
		



path ='/home/tarun/ccbd/ccbd_images/bounding_box_val/*.jpg'   
files=glob.glob(path)
pic = 0
oldpic = 0
flag = 0 
startx=0
starty=0 
endx = 0
endy=0
w=h=0
final_dict = {}
counter = 0
for file2 in files:
	flag=0
	pic = cv2.imread(file2)
	pic = cv2.resize(pic,(1800,1800),interpolation=cv2.INTER_CUBIC)
	oldpic = pic.copy()
	startx=0
	starty=0 
	endx = 0
	endy=0
	w=h=0

	cv2.namedWindow('window',cv2.WINDOW_NORMAL)
	cv2.setMouseCallback('window', click_and_crop)
	while True:
		cv2.imshow('window',pic)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("s"):
			#write values to file
			print startx, starty,w,h
			final_dict[file2] = [startx, starty,w,h]
			counter = counter + 1
			print counter
			cv2.imwrite('./testing.jpg',pic)
			break
		elif key== ord("r"):
			#remove rectangle
			pic = oldpic.copy()
			print 'cleared'
		elif key==ord("n"):
			break					

#pickle.dump(final_dict,open("./bounding_box_val_data.npy","wb"))						