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

img_H, img_W = image.shape[:2]

center_X, center_Y = img_H//2, img_W//2

# circle_center = (center_Y, center_X)
# radius = 100

# cv2.circle(image_circle, circle_center, radius=radius,color=(0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
# cv2.imshow("Circle Image", image_circle)

# DRAWING RECTANGLE TO THE IMAGE

# image_rectangle = image.copy()

# height, width = image.shape[:2]

# rect_width = 200
# rect_height = 100

# center_x = width // 2
# center_y = height // 2

# x1 = center_x - rect_width // 2
# y1 = center_y - rect_height // 2
# x2 = center_x + rect_width // 2
# y2 = center_y + rect_height // 2

# cv2.rectangle(image_rectangle, (x1, y1), (x2, y2), (0,255,0), -1)

# cv2.imshow("Image Having Rectangle", image_rectangle)

# DRAWING ELLIPSE TO THE IMAGE
imageEllipse = image.copy()

ellipse_center = (center_Y, center_X)

axis1 = (100,50)
axis2 = (125,50)


cv2.ellipse(imageEllipse, ellipse_center, axis1, 0, 0, 360, (255, 0, 0), thickness=-1)

cv2.ellipse(imageEllipse, ellipse_center, axis2, 90, 0, 360, (0, 0, 255), thickness=-1)

cv2.imshow('ellipse Image',imageEllipse)
cv2.waitKey(0)
cv2.destroyAllWindows()