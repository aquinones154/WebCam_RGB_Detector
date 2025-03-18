import numpy as np
import cv2
import os

#open camera
cam = cv2.VideoCapture(0)


while True:
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    output = frame.copy()
    rectangle = cv2.rectangle(output,(50,50),(100,100),(0,255,0),4)
    cv2.imshow('rectangle',rectangle)
    
    # mapping the frame to BGR(rgb but in reverse order according to opencv)
    b = frame[:, :, 0]  #blue
    g = frame[:, :, 1]  #green
    r = frame[:, :, 2]  #red

    #getting average of each color
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    if (b_mean > g_mean and b_mean > r_mean):
        print("Blue")
    if (g_mean > b_mean and g_mean > r_mean):
        print("Green")
    else:
        print("Red")


    if ret == False:
        print("Something went wrong")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'): # break the loop when q is pressed
        break

cam.release()
cv2.destroyAllWindows()