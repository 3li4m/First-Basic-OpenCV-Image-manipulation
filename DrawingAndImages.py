import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)


##work in B,G,R
cv2.line(img,(0,0),(150,150),(255,0,255),5)
cv2.rectangle(img,(15,25),(200,150),(255,0,0),2)
cv2.circle(img,(100,400),55,(0,0,255),-1)
cv2.circle(img,(400,400),55,(0,0,255),1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#true is wheather we want to connect the end point with the start
cv2.polylines(img,[pts],True,(0,50,255),3)
#pts = pts.reshape((-1,1,2))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'YAY first CV2 Project',(100,430),font,1,(0,0,0),1,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows();
