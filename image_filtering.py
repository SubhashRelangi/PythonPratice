import cv2
import numpy as np

image = cv2.imread("images/url0.png")

if image is None:
    print("Could not read image.")

# APPLYING THE IDENTITY MATRIX EFFECT TO THE IMAGE USING THE FILTER2D() METHOD
# kernell = np.array([[0,0,0],
#                     [0,1,0],
#                     [0,0,0]])

# identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernell)

# cv2.imshow("Original Image", image)
# cv2.imshow("Identity Image", identity)
# cv2.imwrite("IdentityImage.png", identity)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# APPLYING THE BLUR MATRIX EFFECT TO THE IMAGE USING THE FILTER2D() METHOD

# kernel2 = np.ones((5,5), np.float32) / 25

# img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

# cv2.imshow("Original image", image)
# cv2.imshow("Kernel Blur", img)

# cv2.waitKey(0)
# cv2.imwrite("Blur_Kernel.png", img)

#APPLYING BLUR  EFFECT TO THE IMAGE USING BLUR() METHOD

# img_blur = cv2.blur(src=image, ksize=(5,5))

# cv2.imshow("Original Image", image)
# cv2.imshow("Blur Image", img_blur)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

#APPLYING BLUR EFFECT USING GaussianBlur() METHOD

# gaussian_blur = cv2.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0)

# cv2.imshow("Original Image", image)
# cv2.imshow("GaussianBlur", gaussian_blur)

# cv2.imwrite("images/GaussianBlur.png", gaussian_blur)

#APPLYING BLUR EFFECT USING MEdianBlur() METHOD

median = cv2.medianBlur(src=image, ksize=5)
 
cv2.imshow('Original', image)
cv2.imshow('Median Blurred', median)
     
cv2.waitKey()
cv2.imwrite('median_blur.jpg', median)

cv2.waitKey(0)
cv2.destroyAllWindows()