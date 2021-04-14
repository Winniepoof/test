import cv2 as cv
import facedetect


vid=cv.VideoCapture('soyong1.avi')
while True:
    flag,fram=vid.read()
    if not flag:
        break
    facedetect.change(fram)
    if ord('q')==cv.waitKey(0):
        break
cv.destroyAllWindows()
vid.release()