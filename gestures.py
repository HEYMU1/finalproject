import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

a = [[34.655446902326915, 37.64306044943742, 31.0, 25.179356624028344, 94.33981132056604, 38.2099463490856, 23.345235059857504, 18.973665961010276, 95.50916186418976, 41.23105625617661, 25.0, 21.18962010041709, 91.4166286842826, 39.66106403010388, 25.238858928247925, 21.095023109728988, 86.97700845625813, 33.60059523282288, 22.02271554554524, 20.518284528683193],[36.89173349139343, 42.37924020083418, 37.33630940518894, 27.730849247724095, 100.24470060806208, 41.012193308819754, 24.331050121192877, 20.8806130178211, 99.29753269845128, 42.95346318982906, 26.92582403567252, 22.847319317591726, 93.77632963600144, 41.78516483155236, 27.313000567495326, 21.02379604162864, 86.6083136886985, 32.55764119219941, 22.627416997969522, 20.0],[38.01315561749642, 40.80441152620633, 34.92849839314596, 27.51363298439521, 103.47946656221224, 42.01190307520001, 27.586228448267445, 22.627416997969522, 102.00490184299969, 43.278170016764804, 28.0178514522438, 21.95449840010015, 97.04638066409278, 39.11521443121589, 24.698178070456937, 19.72308292331602, 88.07383266328314, 28.792360097775937, 19.313207915827967, 18.384776310850235],[30.870698080866262, 36.069377593742864, 28.844410203711913, 24.166091947189145, 86.1278120005379, 33.95585369269929, 20.396078054371138, 16.0312195418814, 87.05170877128145, 38.05259518088089, 23.021728866442675, 19.026297590440446, 83.74365647617735, 36.87817782917155, 23.08679276123039, 19.4164878389476, 79.60527620704548, 30.23243291566195, 19.72308292331602, 17.46424919657298],[43.174066289845804, 46.647615158762406, 37.53664875824692, 29.068883707497267, 101.6070863670443, 41.617304093369626, 24.698178070456937, 21.93171219946131, 97.57561170702442, 40.85339643163099, 26.248809496813376, 20.8806130178211, 91.78235124467012, 36.87817782917155, 23.769728648009426, 19.6468827043885, 85.28774824088158, 29.427877939124322, 20.223748416156685, 19.235384061671343]]
def calculate_distance(landmark1, landmark2):
    return np.sqrt((landmark1[0] - landmark2[0])**2 + (landmark1[1] - landmark2[1])**2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    count = 0
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmark_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append([cx, cy])

            distances = []
            j = 1
            while j < 21:
                demodi = []
                demodi.append(landmark_list[0])
                for i in range(j,j+4):
                    demodi.append(landmark_list[i])
                for k in range(4):
                    distance = calculate_distance(demodi[k],demodi[k+1])
                    distances.append(distance)
                j = j+4
            count = 0        
            for l in a:
                count1 = 0
                for i1,j1 in zip(distances,l):
                    b = np.sqrt((i1 - j1)**2)
                    if b <= 4:
                        count1 = count1+1
                if count1 > 15:
                    count = count+1
            if count > 0 :
                gesture = "Hi"
            else :
                gesture = None

            if gesture :
                h, w, c = frame.shape
                y = h - 20
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                text_size, _ = cv2.getTextSize(gesture, font, font_scale, 2)
                x = (w - text_size[0]) // 2
                cv2.putText(frame, gesture, (x,y), font, font_scale, (255, 255, 255), 2)




        
    cv2.imshow('Hand Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

