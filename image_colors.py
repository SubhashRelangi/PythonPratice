import cv2
import numpy as np

bright = cv2.imread("images/cube.png")
# dark = cv2.imread("images/two-cubes.png")

# Color Spaces Conversion into BGR to HSV, YCrCb, LAB

brightLAB = cv2.cvtColor(bright, cv2.COLOR_BGR2LAB)
# darkLAB = cv2.cvtColor(dark, cv2.COLOR_BGR2LAB)

# cv2.imshow("Bright Lab Image", brightLAB)
# cv2.imshow("Dark Lab Image", darkLAB)

cv2.imshow("Original Image", bright)

brightHSV = cv2.cvtColor(bright, cv2.COLOR_BGR2HSV)
# darkHSV = cv2.cvtColor(dark, cv2.COLOR_BGR2HSV)

# cv2.imshow("Bright HSV Image", brightHSV)
# cv2.imshow("Dark HSV Image", darkHSV)

BrightYCRCB = cv2.cvtColor(bright, cv2.COLOR_BGR2YCrCb)
# DarkYCRCB = cv2.cvtColor(dark, cv2.COLOR_BGR2YCrCb)

# cv2.imshow("Bright YCrCb Image",BrightYCRCB)
# cv2.imshow("Dark YCrCb Image",DarkYCRCB)

bgr = [40, 158, 16]
thresh = 40
 
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

# # minBGR = np.array([0, 188, 0])
# # maxBGR = np.array([80, 198, 56])
 
maskBGR = cv2.inRange(bright,minBGR,maxBGR)
resultBGR = cv2.bitwise_and(bright, bright, mask = maskBGR)
 
# #convert 1D array to 3D, then convert it to HSV and take the first element
# # this will be same as shown in the above figure [65, 229, 158]
hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]
 
# minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
# maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])

minHSV = np.array([25, 189, 118])
maxHSV = np.array([95, 225 ,198])
 
maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)
resultHSV = cv2.bitwise_and(brightHSV, brightHSV, mask = maskHSV)
 
# #convert 1D array to 3D, then convert it to YCrCb and take the first element
ycb = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2YCrCb)[0][0]
 
minYCB = np.array([ycb[0] - thresh, ycb[1] - thresh, ycb[2] - thresh])
maxYCB = np.array([ycb[0] + thresh, ycb[1] + thresh, ycb[2] + thresh])
 
maskYCB = cv2.inRange(BrightYCRCB, minYCB, maxYCB)
resultYCB = cv2.bitwise_and(BrightYCRCB, BrightYCRCB, mask = maskYCB)
 
# #convert 1D array to 3D, then convert it to LAB and take the first element
lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]
 
minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])
 
maskLAB = cv2.inRange(brightLAB, minLAB, maxLAB)
resultLAB = cv2.bitwise_and(brightLAB, brightLAB, mask = maskLAB)
 
cv2.imshow("Result BGR", resultBGR)
cv2.imshow("Result HSV", resultHSV)
cv2.imshow("Result YCB", resultYCB)
cv2.imshow("Output LAB", resultLAB)

cv2.waitKey(0)
cv2.destroyAllWindows()