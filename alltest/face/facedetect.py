import cv2 as cv


def change(img):
    gray=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    #cv.imshow('1',gray)
    face_detector=cv.CascadeClassifier('D:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    faces=face_detector.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,225),thickness=2)
    cv.imshow('2',img)