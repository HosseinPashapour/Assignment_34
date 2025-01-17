import cv2

image=cv2.imread("input\Rubik.jpg")

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        R,G,B=image[i,j]

        if R<50 and G>100 and B>100:       
            R=255
            G=0
            B=0 

        elif  R>100 and G<50 and B>100:        
            G=255
            R=0
            B=0

        elif   R>100 and G>100 and B<50: 
            B=255      
            R=0
            G=0    
            
        image[i,j]=R, G, B

cv2.imshow("Rubik", image)
cv2.imwrite("output\Solve_Rubik.jpg", image)
cv2.waitKey()
