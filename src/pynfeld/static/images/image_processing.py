import cv2

img = cv2.imread("doctor.jpeg")

img_resize = cv2.resize(img, (400,500))

print(img_resize.shape)
cv2.imwrite("doctor_resized.jpeg", img_resize)




