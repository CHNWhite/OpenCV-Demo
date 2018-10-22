import cv2
from math import *
import numpy as np

img = cv2.imread("logo.png")

height,width=img.shape[:2]

degree=90
#旋转后的尺寸
heightNew=int(width*fabs(sin(radians(degree)))+height*fabs(cos(radians(degree))))
widthNew=int(height*fabs(sin(radians(degree)))+width*fabs(cos(radians(degree))))

matRotation=cv2.getRotationMatrix2D((width/2,height/2),degree,1)

matRotation[0,2] +=(widthNew-width)/2  #重点在这步，目前不懂为什么加这步
matRotation[1,2] +=(heightNew-height)/2  #重点在这步

imgRotation=cv2.warpAffine(img,matRotation,(widthNew,heightNew),borderValue=(255,255,255))

cv2.imshow("imgRotation",imgRotation)
cv2.waitKey(0)