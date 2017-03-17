
import cv2
import sys

# Get user supplied values
# imagePath = sys.argv[1]
# cascPath = sys.argv[2]

imagePath = 'driver1.png'
# imagePath = 'Driver_License_Janek.jpg'

# cascade path
cascade_face = 'haarcascade_frontalface_default.xml'
cascade_eye = 'haarcascade_eye.xml'
cascade_mouth = 'haarcascade_mcs_mouth.xml'

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascade_face)
eyeCascade = cv2.CascadeClassifier(cascade_eye)
mouthCascade = cv2.CascadeClassifier(cascade_mouth)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

eyes = eyeCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

mouth = mouthCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

for (x, y, w, h) in mouth:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("Faces found" ,image)
cv2.waitKey(0)
