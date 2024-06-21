import cv2
import time
import os
import modules.HandTrackingModule as htm
from playsound import playsound

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

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

        fingerCount = fingers.count(1)
        print(fingerCount)

        if fingerCount == 1:
            playsound('sounds/one.mp3')
            time.sleep(1)
        elif fingerCount == 2:
            playsound('sounds/two.mp3')
            time.sleep(1)
        elif fingerCount == 3:
            playsound('sounds/three.mp3')
            time.sleep(1)
        elif fingerCount == 4:
            playsound('sounds/four.mp3')
            time.sleep(1)
        elif fingerCount == 5:
            playsound('sounds/five.mp3')
            time.sleep(1)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
