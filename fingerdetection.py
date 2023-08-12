import cv2, random, math
import numpy as np
import matplotlib.pyplot as plt
import time

def calculateAngle(far, start, end):
    a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
    c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
    angle = math.acos((b**2 + c**2 - a**2) / (2*b*c))
    return angle

image = cv2.imread("5_P_hgr1_id09_2.png")
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
Min = np.array([5,55,60],np.uint8)
Max = np.array([13,139,198],np.uint8)
mask  =  cv2 . inRange ( imageHSV , Min, Max)
kernel_square = np.ones(None,np.uint8)
kernel_ellipse= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
dilation = cv2.dilate(mask,kernel_ellipse,iterations = 1)
closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel_square)
erosion = cv2.erode(closing,kernel_square,iterations = 1)
contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

if len(contours)>0:
    maxArea = 0
    hull = []
    fingerList = []
    for i in range (len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if area>maxArea : 
            maxArea = area
            ci = i
    cnts = contours[ci]
    hull2 = cv2.convexHull(cnts)

    hull = cv2.convexHull(cnts, returnPoints=False)
    defects = cv2.convexityDefects(cnts, hull)
    moments = cv2.moments(contours[ci])
    #Central mass 
    if moments['m00']!=0:   #m00 moments spatiaux
        cx = int(moments['m10']/moments['m00']) # cx = M10/M00
        cy = int(moments['m01']/moments['m00']) # cy = M01/M00
    centerMass=(cx,cy)
    cv2.circle(image,centerMass,7,[100,0,255],2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image,'Center',tuple(centerMass),font,0.5,(255,255,255),1)

    D = []
    for i in range (len(cnts)):
        x = np.array(cnts[i][0][0])
        y = np.array(cnts[i][0][1])
        xp = np.power(x-cx, 2)
        yp = np.power(y-cy, 2)
        dist = np.sqrt(xp+yp)
        D.append(dist)
    dist_min = np.min(D)
    closest_d = np.where ( D== dist_min)[0]
    closest_p = tuple(cnts[closest_d[0]][0])

    cnt = 0
    farDefect=[]
    Far =[]
    if type(defects) != type(None):
        for i in range (defects.shape[0]):
            s,e,f,d = defects[i, 0]
            start = tuple(cnts [s,0])
            end = tuple(cnts[e,0])
            far = tuple(cnts[f,0])
            Far.append(far)
            x = far[0]
            y = far[0]
            angle = calculateAngle (far, start, end)
            if angle<= math.pi/1.6 and far != closest_p and d>8000 :
                cnt+=1
                farDefect.append(far)


    for i in range (len(farDefect)):
        xd = (farDefect[i][0])
        yd = (farDefect[i][1])
        listDistance = []
        dist = 0
        for j in range (defects.shape[0]):
            s,e,f,d = defects[j,0]
            point = cnts[f][0]
            distance = np.sqrt(np.power(point[0]-centerMass[0],2)+np.power(point[1]-centerMass[1],2))
            distance2 =  np.sqrt(np.power(point[0]-xd,2)+np.power(point[1]-yd,2))
            distance3 = np.sqrt(np.power(xd-centerMass[0],2)+np.power(yd-centerMass[1],2))
            if dist<distance and distance2<distance and distance3<distance and distance3+distance2<=distance+50 :
               if i==0 :
                    dist = distance
                    pn= point
                    listDistance.append((point[0],point[1]))
            if i==1 :
                    distance3 = np.sqrt(np.power(pn[0]-point[0],2)+np.power(pn[1]-point[1],2))
                    if distance3>100:
                        dist = distance
                        pn2= point
                        listDistance.append((point[0],point[1]))
                    if i==2 :
                      distance3 = np.sqrt(np.power(pn[0]-point[0],2)+np.power(pn[1]-point[1],2))
                      distance4 = np.sqrt(np.power(pn2[0]-point[0],2)+np.power(pn2[1]-point[1],2))
                    if distance4>100 and distance3>100:
                        dist = distance
                        pn3= point
                        listDistance.append((point[0],point[1]))
                    if i==3 :
                       distance3 = np.sqrt(np.power(pn[0]-point[0],2)+np.power(pn[1]-point[1],2))
                       distance4 = np.sqrt(np.power(pn2[0]-point[0],2)+np.power(pn2[1]-point[1],2))
                    distance5 = np.sqrt(np.power(pn3[0]-point[0],2)+np.power(pn3[1]-point[1],2))
                    if distance4>100 and distance3>100 and distance5>100:
                       dist = distance
                       listDistance.append((point[0],point[1]))

    
        dist = 1000
        for j in range (len(listDistance)):
            point = listDistance[j]
            distance = np.sqrt(np.power(point[0]-xd,2)+np.power(point[1]-yd,2))
            if distance<dist and distance!=0:
                finger = point
        cv2.circle(image,(finger),7,[100,0,255],2)
        fingerList.append(finger)

dist = 50000   
for j in range (len(fingerList)):
    point = fingerList[j]
    distance = np.sqrt(np.power(point[0]-cx,2)+np.power(point[1]-cy,2))
    if distance<dist:
        dist = distance
        finger = point

x,y,w,h = cv2.boundingRect(cnts)
image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

for i in range (len(farDefect)):
    defaut= farDefect[i]
    cv2.circle(image,defaut,7,[100,0,255],2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image,'D',tuple(defaut),font,0.5,(255,255,255),1)

for i in range (len(contours)):
    color_con = (0,255,0) #green color for contours
    color = (255,0,0) #blue color for convex hull
    cv2.drawContours(image, contours, i, color_con, 1,8, hierarchy)
    #cv2.drawContours(image,[hull2], i, color, 1,8)

cv2.imshow("image", image)
cv2.waitKey(0)