#Miniproject2-->8x8 checker board using numpy and opencv
#using for loop
import numpy as np
import cv2

width=7
height=7
pixels=100

row=(width+1)*pixels
col=(height+1)*pixels
image=np.zeros((col,row,3),dtype=np.uint8)
image.fill(255)
y0=0
fill_color=0
for j in range(0,height+1):
    for i in range(0,width+1):
        x0=i*pixels
        y0=j*pixels
        rect_start=(x0,y0)

        x1=x0+pixels
        y1=y0+pixels
        rect_end=(x1,y1)
        image[y0:y1,x0:x1]=fill_color
        if width%2:
            if i !=width:
                fill_color=(0 if (fill_color==255)else 255)
        else:
            if i !=width+1:
                fill_color=(0 if (fill_color==255)else 255)
cv2.imwrite("%d_Width_%d_Height.jpeg"%(width,height),image)
cv2.imshow("hi",image)

cv2.waitKey()
