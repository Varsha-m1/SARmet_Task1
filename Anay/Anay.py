import numpy as np
import cv2

cap=cv2.VideoCapture('project_video.mp4')
i=0
while cap.isOpened() and i<10 :
    i+=1
    ret,frame=cap.read()
    s="frame_"
    s=s+str(i)
    s=s+".png"
    #print(s)
    #cv2.imshow('img',frame)

    font=cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frame,str(i),(150,150),font,4,(255,255,255),2,cv2.LINE_AA)

    cv2.imwrite(s,frame)
    #print(i)
    print("Completed")
cap.release()
cv2.destroyAllWindows()
