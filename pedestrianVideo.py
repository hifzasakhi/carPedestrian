
# import libraries
from vidgear.gears import CamGear
import cv2

pedestrian_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')

stream = CamGear(source='https://www.youtube.com/watch?v=AGDnufgCR7g',
                 stream_mode=True, logging=True).start()  # YouTube Video URL as input

#videoFile = cv2.VideoCapture('dashcam.mp4')
# infinite loop
while True:

    frame = stream.read()
    # read frames

    # check if frame is None
    if frame is None:
        # if True break the infinite loop
        break

    # do something with frame here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    pedestrian_coordinates = pedestrian_tracker.detectMultiScale(gray)
       
    for (x, y, w, h) in pedestrian_coordinates:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    cv2.imshow("Hifza\'s Pedestrian Detector", frame)
    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        # if 'q' key-pressed break out
        break

cv2.destroyAllWindows()
# close output window

# safely close video stream.
stream.stop()
