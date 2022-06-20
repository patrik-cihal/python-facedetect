import cv2
import time

cap = cv2.VideoCapture(0)

face_locatinos = []

while True:
    start = time.time()
    ret, frame = cap.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

    haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    face_locations = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2)
    for x, y, w, h in face_locations:
        print(face_locations)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('Video', frame)

    # Wait for Enter key to stop
    if cv2.waitKey(25) == 13:
        break

    print("found", len(face_locations), "faces in", time.time()-start, "s")
