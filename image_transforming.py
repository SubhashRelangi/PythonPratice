import cv2

image = cv2.imread("images/url3.png")

height, width = image.shape[:2]
center = (width/2,height/2)

rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=-10)

rotate_image = cv2.warpAffine(image, rotate_matrix, (height, width))

cv2.imshow("Original Image", image)

cv2.imshow("Rotated Image", rotate_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# import numpy as np

# image = cv2.imread("images/url4.png")

# height, width = image.shape[:2]

# tx, ty = width/4, height/4

# translation_matrix = np.array([[1, 0, tx],
#                                [0, 1, ty]])

# translation_image = cv2.warpAffine(image, translation_matrix, (height, width))

# cv2.imshow("Original Image", image)

# cv2.imshow("Translation Image", translation_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
