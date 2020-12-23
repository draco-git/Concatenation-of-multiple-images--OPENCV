import cv2
import numpy as np

#reading various images
#NOTE these images must ne stored in same directory where this file is stored
img1 = cv2.imread('avengers.jpg')
img2 = cv2.imread('car.jpg')
img3 = cv2.imread('balls.jpg')

#create a image_matrix which is 2D array which consists images 
#The ouput will be shown in the order in image_matrix
image_matrix = [[img1,img2,img3],[img1,img2,img3]]
image_matrix1 = [[img1,img2,img3],[img1,img2]]

#defining stacking function
#stacking dunction consist of twon parameters 
#image_matrix :- a matrix of images of same dimensions
#scale :- a constant which decides the dimensions of images in output image i.e output_dim = input_dim * scale
def stacking(image_matrix,scale): 
    
    same_dim_images_matrix = [] # A matrix which consists the images after modifying their dimensions such all image dimensions are same.
    
    max_len = max([len(i) for i in image)_matrix]) # max_len which stores the max len of row in image_matrix
    for i in image_matrix:
        if len(i) == max_len:
            same_dim_images_matrix.append([cv2.resize(j,(512,512)) for j in i]) # resizing every image in image_matrix into same dim
        else:
            n = max_len-len(i) # if a row in image_matrix had less images
            for count in range(n): # then fill the gap with the blank images
                i.append(np.zeros((512,512,3)),np.uint8)
            same_dim_images_matrix.append([cv2.resize(j,(512,512)) for j in i])
            
    scaled_image_matrix = [] # the matrix which stores the scaled images of same dimensions
    for i in same_dim_images_matrix:
        scaled_image_matrix.append([cv2.resize(j,None,scale,scale) for j in i])
        
    stacked_matrix = cv2.vconcat([cv2.hconcat(list_h) for list_h in scaled_image_matrix]) # the final result which contains stacked of images.
    return stacked_matrix

#calling the stacked function
output = stacking(image_matrxi,0.5)

#display the image
cv2.imshow('stacked_image',output)
cv2.waitKey(0)
cv2.displayAllWindows()

        
