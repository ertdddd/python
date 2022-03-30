import cv2
import numpy as np
path='01.png'
img=cv2.imread(path)
cv2.imshow('lunwen',img)
higth,width,tongdao=img.shape[0:3]
erzhihua=cv2.inRange(img,np.array([240,240,240]),np.array([255,255,255]))
cv2.namedWindow('image',0)
cv2.resizeWindow('image',int(width),int(higth))
cv2.imshow('image',erzhihua)
kernel=np.ones((3,3),np.int8)
dilate_res=cv2.dilate(erzhihua,kernel,iterations=1)
image_res=cv2.inpaint(img,dilate_res,5,flags=cv2.INPAINT_TELEA)
cv2.namedWindow('fixed_photo',0)
cv2.resizeWindow('fixed_photo',int(width*2),int(higth*2))
cv2.imshow('newImage',image_res)
cv2.waitKey(0)
cv2.destroyWindow()
