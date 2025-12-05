import cv2

bright = cv2.imread("images/two-cubes.png")
dark = cv2.imread("images/two-cubes.png")

# brightLAB = cv2.cvtColor(bright, cv2.COLOR_BGR2LAB)
# darkLAB = cv2.cvtColor(dark, cv2.COLOR_BGR2LAB)

# cv2.imshow("Bright Lab Image", brightLAB)
# cv2.imshow("Dark Lab Image", darkLAB)

cv2.imshow("Original Image", bright)

# brightHSV = cv2.cvtColor(bright, cv2.COLOR_BGR2HSV)
# darkHSV = cv2.cvtColor(dark, cv2.COLOR_BGR2HSV)

# cv2.imshow("Bright HSV Image", brightHSV)
# cv2.imshow("Dark HSV Image", darkHSV)

BrightYCRCB = cv2.cvtColor(bright, cv2.COLOR_BGR2YCrCb)
DarkYCRCB = cv2.cvtColor(dark, cv2.COLOR_BGR2YCrCb)

cv2.imshow("Bright YCrCb Image",BrightYCRCB)
cv2.imshow("Dark YCrCb Image",DarkYCRCB)

cv2.waitKey(0)
cv2.destroyAllWindows()
