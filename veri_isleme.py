import os 
import pickle
import mediapipe as mp
import cv2

mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
mp_drawing_style=mp.solutions.drawing_styles

hands=mp_hands.Hands(static_image_mode=True,min_detection_confidence=0.3)
# face_mesh = mp.solutions.face_mesh.FaceMesh(static_image_mode=True)
# face_mesh = mp.solutions.face_mesh.FaceMesh(min_detection_confidence=0.2)


DATA_DIR="./data"

data=[]
labels=[]

for dir_ in  os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR,dir_)):
        data_aux=[]
        
        x_=[]
        y_=[]
        
        
        
        img=cv2.imread(os.path.join(DATA_DIR,dir_,img_path))
        img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        
        result=hands.process(img_rgb)
        
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x=hand_landmarks.landmark[i].x
                    y=hand_landmarks.landmark[i].y
                    
                    x_.append(x)
                    y_.append(y)
                
                for i in range(len(hand_landmarks.landmark)):
                    x=hand_landmarks.landmark[i].x
                    y=hand_landmarks.landmark[i].y
                    
                    data_aux.append(x-min(x_))
                    data_aux.append(y-min(y_))
                    
                data.append(data_aux)
                labels.append(dir_)

f=open("data.pickle","wb")
pickle.dump({"data":data,"labels":labels},f)
f.close()



