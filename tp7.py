import numpy as np
import cv2
import sys

		
		
def detect_face(image) :
	face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

	img = cv2.imread(image)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_color = img[y:y+h, x:x+w]
	cv2.imshow('img',img) #roi_color pour ne voir que le visage 
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return faces
	
if __name__ == "__main__" :
	
	if (len(sys.argv) < 2) :
		print("usage python tp7.py nom_fichier")
	else :
		print(detect_face(sys.argv[1]))
		

