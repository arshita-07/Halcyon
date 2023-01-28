import cv2 as cv
img = cv.imread("Photos/park.jpg")
cv.imshow("original",img)
#conv to grey scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("boston",gray)
#blur (remove noise/ bad lighting/ issues w camera sensor)
#to inc blurriness inc the kernel size
blur = cv.GaussianBlur(img, (3,3),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)
#edge cascade
canny = cv.Canny(img, 125,175)
cv.imshow("Canny edges",canny)
#incase you want to decrease the number of edges pass in the blur img
#dilating the img
dilated = cv.dilate(canny, (7,7),iterations=3)
cv.imshow("dilated", dilated)
#erroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow("erroded",eroded)
#resizing
resized = cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
cv.imshow("resized",resized)
#inter_area if you are scaling the image to smaller dimensions. use inter_linear if you have scaling the image to larger dimensions.
#cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped",cropped)
cv.waitKey(0)
