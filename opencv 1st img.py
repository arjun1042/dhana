import cv2
import numpy as np

img=cv2.imread("C:/Users/Dhanarjana/Downloads/apple.jpg", 75)
r,b,g=cv2.split(img)

cv2.imshow("red", r)

cv2.imshow("green", g)

cv2.imshow("blue", b)

merge_image=cv2.merge([r,b,g])

cv2.imshow("merge_image", merge_image)

cv2.waitKey(0)
