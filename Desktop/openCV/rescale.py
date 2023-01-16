#rescaling and resizing of videos and images is done to avoid computational strain
#large sized images and video contain a lot of information that demands high computer resources in order to be displayed
import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA )

#will work for live videos only
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture(0)
while True:
    isTrue, frame= capture.read() #reading frame by frame. the first value is a boolean which contains if the frame wa successfully read or not
    cv.imshow('Video',frame) #displaying frame by frame
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

img = cv.imread("Photos/cat.jpg")
cv.imshow("cat", img)
cv.imshow("cat_resized",rescaleFrame(img))


capture = cv.VideoCapture("Videos/dog.mp4") 
while True:
    isTrue, frame= capture.read() 
    frame_resized = rescaleFrame(frame, scale=0.2)
    cv.imshow('Video',frame)
    cv.imshow('video resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()