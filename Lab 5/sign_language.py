import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
import alsaaudio
m = alsaaudio.Mixer()
################################
wCam, hCam = 640, 480
################################
 
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
 
detector = htm.handDetector(detectionCon=0.7)
minVol = 0
maxVol = 100
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
 
        thumbX, thumbY = lmList[4][1], lmList[4][2] #thumb
        pointerX, pointerY = lmList[8][1], lmList[8][2] #pointer

        middleX, middleY = lmList[12][1], lmList[12][2]
        ringX, ringY = lmList[16][1], lmList[16][2]
        pinkyX, pinkyY = lmList[20][1], lmList[20][2]
        
        cx, cy = (thumbX + pointerX) // 2, (thumbY + pointerY) // 2
 
        cv2.circle(img, (thumbX, thumbY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (pointerX, pointerY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (middleX, middleY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (ringX, ringY), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (pinkyX, pinkyY), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (thumbX, thumbY), (pointerX, pointerY), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        len_calc = lambda x1,y1,x2,y2: math.hypot(x2 - x1, y2 - y1)
        thumb_pointer = len_calc(thumbX,thumbY,pointerX,pointerY)
        pointer_middle = len_calc(pointerX,pointerY,middleX,middleY)
        middle_ring = len_calc(middleX, middleY, ringX, ringY)
        ring_pinky = len_calc(ringX, ringY, pinkyX, pinkyY)
        thumb_ring = len_calc(thumbX,thumbY, ringX, ringY)
        thumb_middle = len_calc(thumbX,thumbY, middleX, middleY)
        thumb_pinky = len_calc(thumbX,thumbY, pinkyX, pinkyY)

        print(pointer_middle,middle_ring,ring_pinky)

        condition_money = thumb_pointer<100 and thumb_middle>100 and thumb_ring>100 and thumb_pinky>100 and middle_ring>50 and ring_pinky>50
        
        if condition_money:
            m.setvolume(0)
            volPer = 0
            volBar = 400
            print("CONDITION")
            cv2.putText(img, 'Money', (40, 100), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)

        condition_yes = thumb_pointer>100 and middle_ring<100 and ring_pinky<100 and pointer_middle>100

        if condition_yes:
            m.setvolume(0)
            volPer = 0
            volBar = 400
            print("CONDITION")
            cv2.putText(img, 'Yes', (40, 100), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)
        
        condition_love = thumb_pointer>100 and pointer_middle>100 and middle_ring<100 and ring_pinky>100
        if condition_love:
            m.setvolume(0)
            volPer = 0
            volBar = 400
            print("CONDITION")
            cv2.putText(img, 'I love you', (40, 100), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)

        condition_i = thumb_pointer<100 and pointer_middle<100 and middle_ring<100 and thumb_pinky>100
        if condition_i:
            m.setvolume(0)
            volPer = 0
            volBar = 400
            print("CONDITION")
            cv2.putText(img, 'I am', (40, 100), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)

        condition_fine = thumb_pointer>100 and pointer_middle<100 and middle_ring<100 and ring_pinky<100
        if condition_fine:
            m.setvolume(0)
            volPer = 0
            volBar = 400
            print("CONDITION")
            cv2.putText(img, 'fine', (40, 100), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)
    
        else:
 
            vol = np.interp(thumb_pointer, [50, 300], [minVol, maxVol])
            volBar = np.interp(thumb_pointer, [50, 300], [400, 150])
            volPer = np.interp(thumb_pointer, [50, 300], [0, 100])
            m.setvolume(int(vol))

        print(int(thumb_pointer), vol)

 
        if thumb_pointer < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
 
    #cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    #cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    #cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
    #            1, (255, 0, 0), 3)
 
 
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
 
    cv2.imshow("Img", img)
    cv2.waitKey(1)