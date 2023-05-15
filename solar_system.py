import cv2

img=cv2.imread('Images/solar-system.jpg')
cv2.putText(img, "Sun", (40,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 2)
cv2.putText(img, "Mercury", (120,190), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(img, "Venus", (200,300), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(img, "Earth", (300,160), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(img, "Mars", (380,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (490,350), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Saturn", (760,300), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(img, "Uranus", (960,140), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.putText(img, "Neptune", (1100,300), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255,255,255))
cv2.imwrite('Solar_SystemwithName.jpg', img)
cv2.imshow("Display Image", img)
cv2.waitKey(0)


while True:
    if cv2.waitKey(25)==32:
     break

