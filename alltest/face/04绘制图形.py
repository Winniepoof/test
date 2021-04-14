'''
画矩形
'''
import cv2 as cv
img=cv.imread('Mikami Yua.jpg')
# x,y,w,h=100,100,100,100
# cv.rectangle(img,(x,y,x+h,y+h),color=(0,225,0),thickness=2)
x,y,r=100,100,100
cv.circle(img,center=(x,y),radius=(r),color=(0,225,0),thickness=2)
cv.imshow('mikami',img)
cv.waitKey(0)
cv.destroyAllWindows()