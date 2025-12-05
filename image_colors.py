import cv2
import numpy as np

bright = cv2.imread("images/two-cubes.png")
dark = cv2.imread("images/two-cubes.png")

# Color Spaces Conversion into BGR to HSV, YCrCb, LAB

brightLAB = cv2.cvtColor(bright, cv2.COLOR_BGR2LAB)
darkLAB = cv2.cvtColor(dark, cv2.COLOR_BGR2LAB)

# cv2.imshow("Bright Lab Image", brightLAB)
# cv2.imshow("Dark Lab Image", darkLAB)

cv2.imshow("Original Image", bright)

brightHSV = cv2.cvtColor(bright, cv2.COLOR_BGR2HSV)
darkHSV = cv2.cvtColor(dark, cv2.COLOR_BGR2HSV)

# cv2.imshow("Bright HSV Image", brightHSV)
# cv2.imshow("Dark HSV Image", darkHSV)

BrightYCRCB = cv2.cvtColor(bright, cv2.COLOR_BGR2YCrCb)
DarkYCRCB = cv2.cvtColor(dark, cv2.COLOR_BGR2YCrCb)

# cv2.imshow("Bright YCrCb Image",BrightYCRCB)
# cv2.imshow("Dark YCrCb Image",DarkYCRCB)

bgr = [10, 10, 16]
thresh = 40

# Segmentation of the colors in the image into the BGR color space
# minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
# maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

# maskBGR = cv2.inRange(bright, minBGR, maxBGR)
# resultBGR = cv2.bitwise_and(bright, bright, mask = maskBGR)

# cv2.imshow("Result BGR", resultBGR)


# Segmentation of the colors in the image into the HSV color space
# hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]

# Compute lower HSV
# minHSV = np.array([
#     max(hsv[0] - thresh, 0),
#     max(hsv[1] - thresh, 0),
#     max(hsv[2] - thresh, 0)
# ])

# Compute upper HSV
# maxHSV = np.array([
#     min(hsv[0] + thresh, 179),
#     min(hsv[1] + thresh, 255),
#     min(hsv[2] + thresh, 255)
# ])


# maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)
# resultHSV = cv2.bitwise_and(brightHSV, brightHSV, mask=maskHSV)

# cv2.imshow("Result HSV", resultHSV)

# Segmentation of the colors in the image into the LAB color space

# lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]
 
# minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
# maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])
 
# maskLAB = cv2.inRange(brightLAB, minLAB, maxLAB)
# resultLAB = cv2.bitwise_and(brightLAB, brightLAB, mask = maskLAB)

# cv2.imshow("Result LAB", resultLAB)

# Segmentation of the colors in the image into the YCrCb color space

ycb = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2YCrCb)[0][0]
 
minYCB = np.array([ycb[0] - thresh, ycb[1] - thresh, ycb[2] - thresh])
maxYCB = np.array([ycb[0] + thresh, ycb[1] + thresh, ycb[2] + thresh])
 
maskYCB = cv2.inRange(BrightYCRCB, minYCB, maxYCB)
resultYCB = cv2.bitwise_and(BrightYCRCB, BrightYCRCB, mask = maskYCB)

cv2.imshow("Result YCrCb", resultYCB)


cv2.waitKey(0)
cv2.destroyAllWindows()
