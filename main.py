import numpy as np
import cv2
import os

# Open the camera
cam = cv2.VideoCapture(0)

# limits to check for special colors
high_limit = 150
low_limit = 100

while True:
    ret, frame = cam.read()
    if not ret:
        print("Something went wrong")
        break

    #might remove this later on
    cv2.imshow('frame', frame)
    output = frame.copy()
    rectangle = cv2.rectangle(output, (50, 50), (100, 100), (0, 255, 0), 4)
    cv2.imshow('rectangle', rectangle)
    
    # mapping the colors
    b = frame[:, :, 0]  
    g = frame[:, :, 1]  
    r = frame[:, :, 2]  

    # getting average of each color
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    # speical colors
    if (b_mean > high_limit and r_mean > high_limit and g_mean < low_limit):
        print("Indigo")
    elif (r_mean > high_limit and g_mean > high_limit and b_mean > high_limit):
        print("White")
    else:
        # if not speical color then return primary color
        if b_mean > g_mean and b_mean > r_mean:
            print("Blue")
        elif g_mean > b_mean and g_mean > r_mean:
            print("Green")
        else:
            print("Red")

    if cv2.waitKey(1) & 0xFF == ord('q'):  # break loop when user prcess 'q' 
        break

cam.release()
cv2.destroyAllWindows()
