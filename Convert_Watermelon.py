import cv2

img = cv2.imread("input\watermelon.jpg")
B, G, R = cv2.split(img)
result = cv2.merge((B, R, G))

cv2.imshow("Materwelon",result)
cv2.imwrite("output\Materwelon.jpg", result)
cv2.waitKey()