import numpy as np
import cv2
import os

#open camera
cam = cv2.VideoCapture(0)


while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)

    if ret == False:
        print("Something went wrong")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'): # break the loop when q is pressed
        break

cam.release()
cv2.destroyAllWindows()