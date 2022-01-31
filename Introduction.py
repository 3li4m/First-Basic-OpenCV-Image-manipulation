import cv2
import numpy as np
import matplotlib.pyplot as plt

#notes also can use
#IMREAD_COLOR = coresponds to 1
#IMREAD_UNCHANGED = -1
#IMREAD_GRAYSCALE = 0

img = cv2.imread('Watch.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite('GrayWatch.jpg',img)

#using matplotlib
##plt.imshow(img,cmap ='gray', interpolation='bicubic')
##plt.plot([50,100],[80,100],'c',linewidth=2)
##plt.show()




