import cv2 as cv
import HandTrackingModule as htm
from cvzone.SerialModule import SerialObject

Arduino_bord = SerialObject("COM4")


cap = cv.VideoCapture(0)
detector = htm.HandDetector(detection=0.2)

while True :
    istrue, frame = cap.read()
    frame = detector.find_hands(frame)
    lmlist = detector.FindPosition(frame)
    # print(lmlist)
    tips = [4,8,12,16,20]
    if len(lmlist) != 0:
        fingure = []
        if lmlist[tips[0]][1] < lmlist[tips[0]-1][1]:
            fingure.append(0)
        else:
            fingure.append(1)
        for id in range(1,5):
            if lmlist[tips[id]][2] < lmlist[tips[id]-2][2]:
                fingure.append(1)
            else:
                fingure.append(0)
        total_fig = fingure.count(1)
        print(total_fig)
        # print(fingure)
        if len(fingure)!=0:
            if total_fig == 5 :
                print("fingures are open")
                Arduino_bord.sendData([1])
            else:
                print("close")
                Arduino_bord.sendData([0])
    cv.imshow("video",frame)
    if cv.waitKey(20) & 0xff == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
        