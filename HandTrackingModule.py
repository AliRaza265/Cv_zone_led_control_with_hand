import cv2 as cv
import mediapipe as mp 
import time

class HandDetector:
    def __init__(self, mode = False, maxhands = 2,detection = 0.5 , trackCon = 0.5):
        self.mode = mode
        self.maxhands = maxhands 
        self.detection = detection
        self.trackCon = trackCon
        self.npHand = mp.solutions.hands
        self.hand = self.npHand.Hands(static_image_mode=self.mode, max_num_hands=self.maxhands,
                                       min_detection_confidence=self.detection, 
                                       min_tracking_confidence=self.trackCon)
        self.mpdraw = mp.solutions.drawing_utils





    def find_hands(self,frame, draw= True):

        img_covt = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        self.result = self.hand.process(img_covt)
        if self.result.multi_hand_landmarks:
            for handslm in self.result.multi_hand_landmarks:
               if draw:
                    self.mpdraw.draw_landmarks(frame,handslm,self.npHand.HAND_CONNECTIONS)
        return frame





    def FindPosition(self,frame,handNo=0,draw = True,):
            lmlist = []

            if self.result.multi_hand_landmarks:
                myhand = self.result.multi_hand_landmarks[handNo]
                for hlm in self.result.multi_hand_landmarks:
                    for index , lm  in enumerate(myhand.landmark):
                        h,w,c = frame.shape
                        cx , cy = int(lm.x * w), int(lm.y * h)
                        # print(index,cx,cy)
                        lmlist.append([index,cx,cy])
                        if draw:
                            cv.circle(frame,(cx,cy),5,(0,0,0),cv.FILLED) 
                                   
            return (lmlist)
   
        


def main():
    capture = cv.VideoCapture(0)
    past_time = 0
    current_time = 0
    detector = HandDetector()
    while True:
        isTrue , frame = capture.read()
        frame = detector.find_hands(frame)
        lmlist = detector.FindPosition(frame)
        if len(lmlist)!=0:
            print(lmlist[3])
        current_time = time.time() 
        fps = 1/(current_time - past_time) 
        cv.putText(frame, str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,255,0),2)
        past_time = current_time 
        print(f'fps {fps}')
        cv.imshow("video",frame)
        if cv.waitKey(20) & 0xff == ord('d'):
            break
    capture.release()
    cv.destroyAllWindows()
if __name__ == "__main__":
    main()
