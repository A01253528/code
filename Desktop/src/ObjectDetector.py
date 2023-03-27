import cv2
import numpy as np

class ObjectRecognition:
    def __init__(self,frameName : str):
        self.cap = cv2.VideoCapture(0)
        self.frameName : str = frameName
        self.stateString = 'No object detect'
        self.matlabState = 0
    def nothing(self,x):
        pass
    def state(self):
         print(self.matlabState)
    def initCamera(self):
        font = cv2.FONT_HERSHEY_COMPLEX
        while True:
            _, frame = self.cap.read()
            hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            lowRed = np.array([161,155,84])
            highRed  = np.array([179,255,255])
            mask = cv2.inRange(hsv, lowRed, highRed)
            kernel = np.ones((5,5), np.uint8)
            mask = cv2.erode(mask, kernel)
            contours, hierachy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                area = cv2.contourArea(cnt)
                approx = cv2.approxPolyDP(cnt,0.02*cv2.arcLength(cnt, True), True)
                x = approx.ravel()[0]
                y = approx.ravel()[1]

                if area > 400:
                    cv2.drawContours(frame, [approx],0,(0,0,0),5)
                    if len(approx) == 3:
                        self.stateString = 'triangle'
                        self.matlabState = 2
                        cv2.putText(frame, "Triangle",(x,y), font,1,(0,0,0))
                    elif len(approx) == 4:
                        self.stateString = 'rectangle'
                        self.matlabState = 2
                        cv2.putText(frame, "Rectangle",(x,y), font,1,(0,0,0))                    
                    elif 10 < len(approx) < 20:
                        cv2.putText(frame, "Circle",(x,y), font,1,(0,0,0))
                        self.stateString = 'circle'
                        self.matlabState = 1
                    else:
                        cv2.putText(frame, "No object detect",(x,y), font,1,(0,0,0))
                        self.stateString = 'No object detect'
                        self.matlabState = 0
            cv2.imshow(self.frameName,frame)
            cv2.imshow("Mask", mask)
            #print(self.stateString)
            print (f"State: {self.state()}")
            key = cv2.waitKey(1)
            if key == 27:
                break
        self.cap.release()
        cv2.destroyAllWindows()
