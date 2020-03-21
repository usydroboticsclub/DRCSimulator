import simulatorInterface
import cv2

def controller(image):
    cv2.imshow("car view",image)
    cv2.waitKey(1)
    
    controlCommand={}
    controlCommand["speed"]=100
    controlCommand["steer"]=0.5
    return controlCommand

simulatorInterface.onMessage(controller)

simulatorInterface.start()