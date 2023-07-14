import keyboard

import cv2
import mediapipe as mp
import math


cap=cv2.VideoCapture(0)

mpHands=mp.solutions.hands     
hands=mpHands.Hands()            #creating object from hands class
mpDraw=mp.solutions.drawing_utils

    #framerate
#pTime=0     #previous time=0
#cTime=0     #current time=0

while True:
    success, img=cap.read()     #read image from camera

    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  #sending PGB img to the hand object first convert it here
    results=hands.process(imgRGB)

    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):       #lm is landmark and id is its id
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)         #cx and cy are centre locations in terms of pixls
                #print(id,cx,cy)

                if id==8:
                    #print("id9",cx,cy)
                    x1,y1=cx,cy
                    cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)
                
                if id==4:
                    #print("id10",cx,cy)
                    x2,y2=cx,cy
                    cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)

                '''if id==11:
                    print("id11",cx,cy)
                    x3,y3=cx,cy
                    cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)'''

                '''if id==12:
                    #print("id12",cx,cy)
                    x3,y3=cx,cy
                    cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)'''


    def angle_between_points(x1, y1, x2, y2, x3, y3):
    #dot product of vectors BA and BC
        dot_product = (x1 - x2) * (x3 - x2) + (y1 - y2) * (y3 - y2)
    
    #magnitudes of vectors BA and BC
        magnitude_ba = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        magnitude_bc = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    
    #cos of the angle between BA and BC
        cosine_angle = dot_product / (magnitude_ba * magnitude_bc)
    
    #angle in radians
        angle_radians = math.acos(cosine_angle)
    
    #angle to degrees
        angle_degrees = math.degrees(angle_radians)
    
        return angle_degrees
    
    '''a=angle_between_points(x1,y1,x2,y2,x3,y3)
    print(int(a))
    m=(int(a)//1)*1'''

    '''rotateservo(pin,m)'''

    '''if a<=90:
        if keyboard.is_pressed('a'):
            keyboard.release('a')
        keyboard.press('z')
        
    if a>90:
        keyboard.release('z')
        keyboard.press('a')
'''

    x=x1-x2
    print(x)

    if x>45:
        keyboard.press('m')
        

    if -45<=x<=45:
        keyboard.release('m')
        keyboard.release('n')


    if x<-45:
        keyboard.press('n')
        

    cv2.imshow('Image',img)     #dispaly the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

