import cv2 as cv
import numpy as np

#读入图片文件
src=cv.imread('thumbnail.jpg')
#创建一个名字加 “ input image ” 的窗口，
# 窗口可以根据图片大小自动调整
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
#在窗口显示图片
cv.imshow('input image',src)

#等待用户操作
cv.waitKey(0)
#释放所有窗口
cv.destroyAllWindows()


# demo2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
