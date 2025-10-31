import cv2
import numpy as np
import bounds_controls # Окошко со слайдерами :3
from math import floor

lower_bound = np.array([330/2, 255*0.75, 255*0.25])
higher_bound = np.array([20/2, 255, 255])

controls = bounds_controls.BoundsControls()
controls.mainloop()

# Задача 1
cap = cv2.VideoCapture(0,cv2.CAP_ANY)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
while cap.isOpened():

    ret,frame = cap.read()
    
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_bound = controls.lower_bound
    higher_bound = controls.higher_bound
    
    # Задача 2
    frame_thresholded = cv2.inRange(frame_hsv,lower_bound,higher_bound)

    # Задача 3
    circle_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    # Открытие
    frame_opened = cv2.erode(frame_thresholded,circle_kernel)
    frame_opened = cv2.dilate(frame_opened,circle_kernel)
    # Закрытие
    frame_closed = cv2.dilate(frame_opened,circle_kernel)
    frame_closed = cv2.erode(frame_closed,circle_kernel)   
    
    # Задача 4
    Moments = cv2.moments(frame_thresholded)
    m01 = Moments['m01']/255 # Изображение не нормировано в [0;1], на деле [0;255]
    m10 = Moments['m10']/255
    area = Moments['m00']/255
    
    # Center
    if(area>0):
        posX = m10/area
        posY = m01/area
        areaPortion = area/(320*240)
        controls.textArea.set(f"{floor(area*100)/100} ({floor(areaPortion*10000)/10000})")
        controls.textPos.set(f"({floor(posX*100)/100}, {floor(posY*100)/100})")
        # Задача 5
        contours,hierarchy = cv2.findContours(frame_closed,1,2)
        if(len(contours)>0):
            cnt = contours[0]
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)

    cv2.imshow("Red mask", frame_opened)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        controls.window.destroy()
        controls.window.quit()
        break

cap.release()