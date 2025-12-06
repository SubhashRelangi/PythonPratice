import cv2
import numpy as np

image = cv2.imread("images/url0.png")

if image is None:
    print("Could not read image.")

kernell = np.array([[1,0,0],
                    [0,1,0],
                    [0,0,1]])

identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernell)

cv2.imshow("Original Image", image)
cv2.imshow("Identity Image", identity)
cv2.imwrite("IdentityImage.png", identity)

cv2.waitKey(0)
cv2.destroyAllWindows()

# kernel2 = np.ones((5,5), np.float32) / 25

# img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)

# cv2.imshow("Original image", image)
# cv2.imshow("Kernel Blur", img)

# cv2.waitKey(0)
# cv2.imwrite("Blur_Kernel.png", img)