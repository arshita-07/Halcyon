import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img) 
#opens a new window. the first parameter is the window name and the second parameter is the image matrix
cv.waitKey(0) #waits for an infinite time in ms for a key to be pressed before closing the window
capture = cv.VideoCapture("Videos/dog.mp4") #this takes 2 types of arguments. either a path to the video or an integer which is used if you wanna capture a video using your webcam
#capture = cv.VideoCapture(0)
while True:
    isTrue, frame= capture.read() #reading frame by frame. the first value is a boolean which contains if the frame wa successfully read or not
    cv.imshow('Video',frame) #displaying frame by frame
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()