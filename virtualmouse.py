import cv2
import mediapipe as mp
import pyautogui
import time 

wcam, hcam = 648, 480
screenw , screenh = pyautogui.size()
hand = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
ptime =0
x1  = y2 = x2 = y2 = 0


while True:
    _, img = cap.read()
    imgh, imgw, _ = img.shape
    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    outputhands = hand.process(rgb)
    allhands = outputhands.multi_hand_landmarks

    if allhands:
        for han in allhands:
            draw.draw_landmarks(img, han)
            onehand = han.landmark
            for id, lm in enumerate(onehand):
                x = int(lm.x * imgw)
                y = int(lm.y * imgh)
                if id == 8:
                    mousex = int(screenw / screenh * x)
                    mousey = int(screenw / screenh * y)
                    cv2.circle(img, (x, y), 7, (0,255,0),3)
                    pyautogui.moveTo(mousex, mousey)
                    x1 = x
                    y1 = y
                if id == 4:
                    x2 = x
                    y2 = y
                    cv2.circle(img, (x, y), 7, (0,255,0),3)
                if id == 12:
                    x3 = x
                    y3 = y
                    cv2.circle(img, (x, y), 7, (0,255,0),3)

        dist = y2-y1
        dist2 = y3 - y1
        print(dist2)
        if dist < 30 : 
            pyautogui.click()
        elif dist< 17:
            pyautogui.doubleClick()
        if dist2 > -20 :
            pyautogui.click(button='secondary')


    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, str(int(fps)),(30,50), cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,0),3)
    cv2.imshow('image', img)

    if cv2.waitKey(1) == ord('q'):
        break