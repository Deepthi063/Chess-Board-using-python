import numpy as np
import cv2


b=np.ones([720,720],dtype='uint8')*255
for i in range(90,720,90*2):
    for j in range(90,720,90*2):
        b[j-90:j,i-90:i]=0
        b[j:j+90,i:i+90]=0
cv2.imshow('Chessboard',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
