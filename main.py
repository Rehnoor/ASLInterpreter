import cv2
import mediapipe as mp



# sig = cv2.imread(filename="pic.png") # Reads file in
# cv2.imshow("my sig", sig) #shows image as a window
# cv2.imwrite("picYo.jpeg", sig) #makes a copy of your image called picYo.img
# cv2.waitKey() #waits for a key before halting
# cv2.destroyAllWindows() #gets rid of windows


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

mp_drawing = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
hand = mp_hand.Hands()


while True:
    success, frame = cap.read()
    if (success):
        RGB_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(RGB_frame)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                print(hand_landmarks)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)
        cv2.imshow("capture img", frame)
        if (cv2.waitKey(1) == ord('q')):
            break


cv2.destroyAllWindows()