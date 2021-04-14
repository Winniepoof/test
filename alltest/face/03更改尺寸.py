import cv2 as cv
img=cv.imread('Mikami Yua.jpg')
cv.imshow('mikami',img)
print(img.shape)
img1=cv.resize(img,dsize=(100,200))
cv.imshow('resize',img1)
print(img1.shape)
while True:
    if ord('q')==cv.waitKey(0):
        break
cv.destroyAllWindows()