from email.mime import image
import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshort():
    number = random.randint(0,50)
    videocapturingobject=cv2.VideoCapture(0)
    result=(True)
    while(result):
        ret, frame = videocapturingobject.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        start_time=time.time
        result=(False)
    return imagename
    print("your snapshot is taken")
    
    videocapturingobject.release()
    cv2.destroyAllWindows()

take_snapshort()