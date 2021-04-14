import cv2 as cv
img=cv.imread('Mikami Yua.jpg')
cv.imshow('pic',img)
img2=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('pic2',img2)
cv.imwrite('Mikami Yua_gray.jpg',img2)
cv.waitKey(0)
cv.destroyAllWindows()