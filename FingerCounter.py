import cv2
import time
import os
import HandTrackingModule as htm
from playsound import playsound

wCam, hCam = 640, 480

cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)


pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        print(fingers)
        if fingers.count(1) == 1:
            playsound(r'sounds\one.mp3')
            time.sleep(1)
        if fingers.count(1) == 2:
            playsound(r'sounds\two.mp3')
            time.sleep(1)    
        if fingers.count(1) == 3:
            playsound(r'sounds\three.mp3')
            time.sleep(1)     
        if fingers.count(1) == 4:
            playsound(r'sounds\four.mp3')
            time.sleep(1)   
        if fingers.count(1) == 5:
            playsound(r'sounds\five.mp3')
            time.sleep(1)      

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break