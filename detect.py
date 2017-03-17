
import cv2
import sys

# Get user supplied values
if sys.argv.__len__() > 1:
    imagePath = sys.argv[1]
    # imagePath = '2.jpg'
    f_video = False
else:
    f_video = True

cal = 1

# cascade path
cascade_face = 'haarcascade_frontalface_default.xml'
cascade_eye = 'haarcascade_eye.xml'
cascade_mouth = 'haarcascade_mcs_mouth.xml'

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascade_face)
eyeCascade = cv2.CascadeClassifier(cascade_eye)
mouthCascade = cv2.CascadeClassifier(cascade_mouth)

if f_video:
    cap = cv2.VideoCapture(0)

while True:
    if f_video:
        ret, image = cap.read()
    else:
        image = cv2.imread(imagePath)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100),
        flags=2
    )

    eyes = eyeCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=2
    )

    mouth = mouthCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=2
    )

    if cal == 1:
        if faces.__len__() > 0:
            face_data = [faces[0]]
        else:
            face_data = [[0, 0, 0, 0]]

        eye_data = []
        for (x, y, w, h) in eyes:
            if x > face_data[0][0] and (x + w) < (face_data[0][0] + face_data[0][2]):           # out of x direction
                if y > face_data[0][1] and (y + h) < (face_data[0][1] + face_data[0][3]):       # out of y direction
                    if (y + h/2) < (face_data[0][1] + face_data[0][3]/2):                       # below face
                        eye_data.append([x, y, w, h])

        mouth_data = []
        for (x, y, w, h) in mouth:
            if x > face_data[0][0] and x + w < face_data[0][0] + face_data[0][2]:               # out of x direction
                if y + h/2 < face_data[0][1] + face_data[0][3]:                                 # out of y direction
                    if y > face_data[0][1] + face_data[0][3]/2:
                        if y < face_data[0][1] + face_data[0][3]:
                            mouth_data.append([x, y, w, h])

    else:
        face_data = faces
        eye_data = eyes
        mouth_data = mouth

    # Draw a rectangle around the faces
    for (x, y, w, h) in face_data:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    for (x, y, w, h) in eye_data:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for (x, y, w, h) in mouth_data:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("Faces found", image)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
