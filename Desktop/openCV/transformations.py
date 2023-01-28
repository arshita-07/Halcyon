import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("boston",img)

#shifting the img
def translate(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#-x left x right
#-y down y up

translated = translate(img,100,100)
cv.imshow("translated", translated)

#rotation
def rotate(img, angle, rotationPoint=None):
    (height,width) = img.shape[:2]
    if rotationPoint is None:
        rotationPoint=(width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotationPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,45)
cv.imshow("rotated",rotated)

#flip
flip = cv.flip(img, -1) # 0 - flip vertically 1 - flip horizontally -1 - flip both vertically and horizontally
cv.imshow("flipped",flip)

#cropping
cropped = img[200:500, 300:400]
cv.imshow("cropped",cropped)
cv.waitKey(0)
