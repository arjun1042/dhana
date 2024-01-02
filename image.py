"""import cv2
img=cv2.imread("D:\arjun.jpg")
clahe=cv2.createCLAHE()
# convert gray scale image
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#APPLY ENHANCEENT
enh_img=clahe.apply(gray_img)
#save to file
cv2.imwrite("enhanced.jpg", enh_img)
print("done enhancing")
cv2.imshow('image',img, size.width>0 & size.height>0)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""


from PIL import Image
img=Image.open("D:\arjun.jpg")
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
transposed_img.save("D:\arjun.jpg")
print("done flipping")
