import cv2
from cvzone.HandTrackingModule import HandDetector
from directkeys import PressKey, ReleaseKey, space_pressed
import time

detector = HandDetector(detectionCon=0.8, maxHands=1)
space_key_pressed = space_pressed

time.sleep(2.0)
current_key_pressed = set()

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    keyPressed = False
    spacePressed = False
    key_pressed = 0
    hands, img = detector.findHands(frame)
    
    cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)
    
    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)
        print(fingerUp)
        
        if fingerUp==[0,1,0,0,0]:
            cv2.putText(frame, 'Finger Count: 1', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Not Jumping', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp==[0,1,1,0,0]:
            cv2.putText(frame, 'Finger Count: 2', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Shoote', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp==[0,1,1,1,0]:
            cv2.putText(frame, 'Finger Count: 3', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Jump', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp==[0,1,1,1,1]:
            cv2.putText(frame, 'Finger Count: 4', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'Run', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
        if fingerUp==[1,1,1,1,1]:
            cv2.putText(frame, 'Finger Count: 5', (20,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'jump Run', (420,460), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1, cv2.LINE_AA)

    if not keyPressed and current_key_pressed:
        for key in current_key_pressed:
            ReleaseKey(key)
        current_key_pressed.clear()

    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
