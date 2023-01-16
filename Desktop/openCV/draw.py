import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow("blank",blank)
blank[200:300, 300:400]=255,0,0
cv.imshow("red",blank)
cv.rectangle(blank,(0,0),(200,200),(0,0,255),cv.FILLED)
cv.imshow("rect",blank)
cv.circle(blank,(250,250),200,(0,255,0),-1)
cv.imshow("circle",blank)
cv.line(blank,(0,0),(250,250),(255,255,255),2)
cv.imshow("line",blank)
cv.putText(blank,"Arshita",(250,250),cv.FONT_HERSHEY_TRIPLEX,1,(200,200,200),5)
cv.imshow("text",blank)
cv.waitKey(0)