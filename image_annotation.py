import cv2

image = cv2.imread('images/url4.png')

cv2.imshow("Original Image", image)
cv2.waitKey(0)

if image is None:
    print("Could not read image.")

# DRAWING LINE TO THE IMAGE

# image_line = image.copy()

# pointA = (200, 80)
# pointB = (450, 180)

# cv2.line(image_line, pointA, pointB, (0, 0, 0), thickness=1, lineType=cv2.LINE_AA)

# cv2.imshow("Image Line", image_line)

# DRAWING CIRCLE TO THE  IMAGE 

# image_circle = image.copy()

# img_H, img_W = image.shape[:2]

# center_X, center_Y = img_H//2, img_W//2

# circle_center = (center_Y, center_X)
# radius = 100

# cv2.circle(image_circle, circle_center, radius=radius,color=(0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
# cv2.imshow("Circle Image", image_circle)

# DRAWING RECTANGLE TO THE IMAGE

image_rectangle = image.copy()
start = (300,115)
end = (475,225)

cv2.rectangle(image_rectangle, start, end, color=(0, 0, 0), thickness=2, lineType=cv2.LINE_AA)


cv2.imshow("Image Having Rectangle", image_rectangle)
cv2.waitKey(0)