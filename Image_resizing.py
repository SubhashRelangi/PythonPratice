
import cv2
import numpy as np

image = cv2.imread("images/url0.png")

print("Original Image Size: ", image.shape)
cv2.imshow("Original Image", image)

resizing = (300, 200)

resize_end = cv2.resize(image, resizing, interpolation=cv2.INTER_LINEAR)

print("Resized-Down values: ", resizing)
cv2.imshow("Resized-Down", resize_end)

resizing_d = (600, 400)

resize_Up = cv2.resize(image, resizing_d, interpolation=cv2.INTER_LINEAR)

print("Resized-Up value: ", resizing_d)
cv2.imshow("Resized-Up", resize_Up)

scale_up_x = 1.2
scale_up_y = 1.2

scale_down = 0.6
 
scaled_f_down = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)

print("scaled_f_down values: ", scale_down)
cv2.imshow("scaled_f_down", scaled_f_down)

scaled_f_up = cv2.resize(image, None, fx= scale_up_x, fy= scale_up_y, interpolation= cv2.INTER_LINEAR)

print("scaled_f_up values: ", "(", scale_up_x, ",", scale_up_y, ")")
cv2.imshow("scaled_f_up", scaled_f_up)

res_inter_nearest = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_NEAREST)
res_inter_linear = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
res_inter_area = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_AREA)

vertical= np.concatenate((res_inter_nearest, res_inter_linear, res_inter_area), axis = 1)
# Display the image Press any key to continue
cv2.imshow('Inter Nearest :: Inter Linear :: Inter Area', vertical)



cv2.waitKey(0)

cv2.destroyAllWindows()