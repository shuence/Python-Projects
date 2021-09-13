import cv2

image =cv2.imread ("C:\\Users\\lenovo\\Pictures\\FBMJADZ.jpg")

resized = cv2.resize(image, (int(image.shape[1]*2), int(image.shape[0]*2)))

cv2.imshow("legend" , image)
cv2.waitKey(0)
cv2.destroyAllWindows

