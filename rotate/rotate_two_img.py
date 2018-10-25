import cv2
from math import *
import time
import  numpy as np



def picprint(fp):


    # Load two images
    img1 = cv2.imread(fp)
    # 创建一个512*512的大小
    # img1 = np.zeros((419,297,3),np.uint8)
    # 图片填充白色
    # img1.fill(255)
    img2 = cv2.imread('test.jpg')
    img2 = cv2.resize(img2,(900,900))

    height,width=img2.shape[:2]

    degree=90
    # 旋转后的尺寸
    heightNew=int(width*fabs(sin(radians(degree)))+height*fabs(cos(radians(degree))))
    widthNew=int(height*fabs(sin(radians(degree)))+width*fabs(cos(radians(degree))))

    matRotation=cv2.getRotationMatrix2D((width/2,height/2),degree,1)

    matRotation[0,2] +=(widthNew-width)/2  # 重点在这步，目前不懂为什么加这步
    matRotation[1,2] +=(heightNew-height)/2  # 重点在这步

    img2=cv2.warpAffine(img2,matRotation,(widthNew,heightNew),borderValue=(255,255,255))

    # I want to put logo on top-left corner, So I create a ROI
    # 把img2放在左上角，创建一个ROI
    rows,cols,channels = img2.shape
    roi = img1[0:rows, 0:cols ]

    # Now create a mask of logo and create its inverse mask also
    # 现在创建一个标志的蒙版，并创建它的反向蒙版
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    # 把ROI区域的img2涂黑
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # Take only region of logo from logo image.
    # 仅从标识图像中提取标识区域。
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

    # Put logo in ROI and modify the main image
    # 将img2放到ROI区域，修改主图像
    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols ] = dst

    # cv2.imshow('res',img1)
    fp = "%s.jpg" % str(time.time())
    cv2.imwrite(fp, img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return fp


if __name__ == '__main__':
    fp = 'baidu.jpg'
    r = picprint(fp)
    print(r)