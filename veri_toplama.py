import os 
import cv2

DATA_DIR="./data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_class=4
data_size=100

cap=cv2.VideoCapture(0) # 0 bilgisayar bagli 1. kamera cihazini temsil ediyor

for j in range(number_of_class):
    if not os.path.exists(os.path.join(DATA_DIR,str(j))):
        os.mkdir(os.path.join(DATA_DIR,str(j)))

    print("data siniflari {}",format(j))
    
    while True:
        _,frame=cap.read()
        cv2.putText(frame,"hazir olunca q bas",(100,50),cv2.FONT_HERSHEY_SIMPLEX,1.3,(0,0,255),3) # kullanilan metnin tipini temsil eder
        # cv2.destroyAIWindows()
        
        cv2.imshow("frame",frame)
        if cv2.waitKey(25) & 0xFF==ord("q"):
            break
                
    counter=0
     
    while counter<data_size:
        _,frame=cap.read()
        cv2.imshow("frame",frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR,str(j),"{}.jpg".format(counter)),frame)
         
        counter+=1
cap.release()
cv2.destroyAllWindows()

   
      


            