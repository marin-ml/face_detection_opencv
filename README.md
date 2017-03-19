# README #

This is the project to detect and save the face, eyes, mouth from image or webcam.

### Requested Library ###

* Python 2.7
* openCV 3

### How can I run this script? ###

This python script can bu run as two modes, one is using of image and the other one is using webcam.

* using image

In case of this mode, we should type the command as belows.

    pyton detect.py image_name

for example

    pyton detect.py my_face.png

* Using webcam

If we don't set the argument in command line, this script run as webcam mode automatically.

    python detect.py

Thanks for you careful look.

* Note

    This script has two main parameter inside.

    - cal

        0: detect and display without calibration.
        1: detect and display with calibration.

    - save_image

        0: Don't save image.
        1: Save image.
