import cv2
vidcap = cv2.VideoCapture("project_video.mp4")
res,frame=vidcap.read()
font=cv2.FONT_HERSHEY_DUPLEX
count = 1
frame=cv2.putText(frame, "%d"%count, (500,300), font, 3.0, (255,0,0), 5)
cv2.imshow("frame_%d"%count,frame)
while count<=10:
  cv2.imwrite("frame_%d.png" % count, frame)
  success,frame = vidcap.read()
  count += 1
  frame=cv2.putText(frame, "%d"%count, (500,300), font, 3.0, (255,0,0), 5)
  cv2.waitKey(0)
  cv2.imshow("frame_%d"%count,frame)
  print('Frame successfully read: ', res)
  
vidcap.release()
cv2.destroyAllWindows()
