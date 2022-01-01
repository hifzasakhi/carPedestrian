

import cv2
from random import randrange 

#making a classifier
#using openCV's existing forntal face classifier algo on pre-trained data
car_tracker = cv2.CascadeClassifier('cars.xml')

#pass the image of the video stream or picture into this aforementioned classifier
img = cv2.imread('cars.jpg')


gray_cars = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#img2 is being changed with the rectangles drawn on them 
car_coordinates = car_tracker.detectMultiScale(gray_cars)
#looping through all faces and then do the pictures
for (x,y,w,h) in car_coordinates:
	#cv2.rectangle(img2, (x,y), (x+w, y+eh), (0,255,0), 5)
	#alternatively, randomly select the color of the drawn rectangle 
	cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
cv2.imshow("Hifza\'s Car Detector", img)
cv2.waitKey()

print("Code completed!")