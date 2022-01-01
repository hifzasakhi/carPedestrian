
# import libraries
from vidgear.gears import CamGear
import cv2

car_tracker = cv2.CascadeClassifier('cars.xml')
pedestrian_tracker = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# define suitable tweak parameters for your stream.
options = {
    "CAP_PROP_FRAME_WIDTH": 320,
    "CAP_PROP_FRAME_HEIGHT": 60,
    "CAP_PROP_FPS": 20,
}

youtube_link = "https://www.youtube.com/watch?v=bq-k_-2GJ2E"
#youtube_link = "https://www.youtube.com/watch?v=WriuvU1rXkc&t"

stream = CamGear(source=youtube_link,
                 stream_mode=True, logging=False, **options).start()  # YouTube Video URL as input

#videoFile = cv2.VideoCapture('dashcam.mp4')

while True:

    frame = stream.read()
    # read frames

    # check if frame is None
    if frame is None:
        # if True break the infinite loop
        break

    # do something with frame here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    car_coordinates = car_tracker.detectMultiScale(gray)
    pedestrian_coordinates = pedestrian_tracker.detectMultiScale(gray)
       
    for (x, y, w, h) in car_coordinates:
         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    #yellow rectangle around the pedestrians 
    for (x, y, w, h) in pedestrian_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 5)


    cv2.imshow("Hifza\'s Car + Pedestrian Video Detector", frame)
    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        # if 'q' key-pressed break out
        break

cv2.destroyAllWindows()
# close output window

# safely close video stream.
stream.stop()
