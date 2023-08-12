import cv2
import numpy as np
import face_recognition
import os

path = ""
images = []
classname = []
mylist = os.listdir(path)

for cl in mylist:
   curimg = cv2.imread(f"{path}/{cl}")
   images.append(curimg)
   classname.append(os.path.splitext(cl)[0])
   print(classname)


def findencoding(images):
   encodelist = []
   for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodelist.append(encode)
    return encodelist


cv2.imshow("webcam",images)
cv2.waitKey(1)
