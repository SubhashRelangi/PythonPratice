import cv2
import numpy as np

image = cv2.imread("images/url2.png")
print("Original Image Shape: ", image.shape)
cv2.imshow("Original Image", image)

cropping = image[80:280, 150:330]

cv2.imshow("Cropped Image", cropping)

cv2.imwrite("images/Cropped_Image.png", cropping)

image_copy = image.copy()

img_H = image.shape[0]
img_W = image.shape[1]

M = 100
N = 100
x1 = 0
y1 = 0
 
for y in range(0, img_H, M):
    for x in range(0, img_W, N):
        if (img_H - y) < M or (img_W - x) < N:
            break
             
        y1 = y + M
        x1 = x + N
 
        # check whether the patch width or height exceeds the image width or height
        if x1 >= img_W and y1 >= img_H:
            x1 = img_W - 1
            y1 = img_H - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        elif y1 >= img_H: # when patch height exceeds the image height
            y1 = img_H - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        elif x1 >= img_W: # when patch width exceeds the image width
            x1 = img_W - 1
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)
        else:
            #Crop into patches of size MxN
            tiles = image_copy[y:y+M, x:x+N]
            #Save each patch into file directory
            cv2.imwrite('saved_patches/'+'tile'+str(x)+'_'+str(y)+'.jpg', tiles)
            cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 1)

cv2.imshow("Patched Image",image)
cv2.imwrite("patched.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows()