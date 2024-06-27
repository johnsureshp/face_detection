import cv2

print('Package imported')
face = cv2.CascadeClassifier('Resource/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,440)
cap.set(10,150)

while True:
    success,img = cap.read()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(imgray, 1.1, 4)


    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 3)
        cv2.putText(img,'preson',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)

    cv2.imshow("result", img)
    if cv2.waitKey(1) & 0xFF == ord('j'):
        break