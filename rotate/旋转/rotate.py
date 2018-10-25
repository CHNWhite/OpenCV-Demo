import cv2
from math import *
import numpy as np

img = cv2.imread("logo.png")

height,width=img.shape[:2]

degree=90
#��ת��ĳߴ�
heightNew=int(width*fabs(sin(radians(degree)))+height*fabs(cos(radians(degree))))
widthNew=int(height*fabs(sin(radians(degree)))+width*fabs(cos(radians(degree))))

matRotation=cv2.getRotationMatrix2D((width/2,height/2),degree,1)

matRotation[0,2] +=(widthNew-width)/2  #�ص����ⲽ��Ŀǰ����Ϊʲô���ⲽ
matRotation[1,2] +=(heightNew-height)/2  #�ص����ⲽ

imgRotation=cv2.warpAffine(img,matRotation,(widthNew,heightNew),borderValue=(255,255,255))

cv2.imshow("imgRotation",imgRotation)
cv2.waitKey(0)