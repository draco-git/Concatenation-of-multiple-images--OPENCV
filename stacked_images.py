import cv2
import numpy as np
import import_images

imgArray = import_images.allImages() # returns resource\image.png array
#print(imgArray,len(imgArray))
imgArray = np.array(imgArray)


def stacking(imgArray,matrix,scale,isGray):
    if isGray == False:
        imageMatrix = imgArray.reshape((matrix[1],matrix[0]))
        imgArrays = [cv2.imread(i) for i in imgArray]
        min_dim  = min([i.shape for i in imgArrays])
        max_dim = max([i.shape for i in imgArrays])
        avg_dim = (sum([(i.shape[0]) for i in imgArrays])//len(imgArrays),sum([(i.shape[1]) for i in imgArrays])//len(imgArrays))
        print([i.shape for i in imgArrays])
        print('min',min_dim,'max',max_dim,'avg',avg_dim)
        same_size_imgArrays = [cv2.resize(i,(1080,720)) for i in imgArrays]
        imgArrays = [cv2.resize(i,(0,0),None,scale,scale) for i in same_size_imgArrays]
        n = matrix[1]
        image_arrays=[]
        for i in range(0,len(imgArrays),n):
            image_arrays.append(imgArrays[i:i+n])
        img = cv2.vconcat([cv2.hconcat(list_h) for list_h in image_arrays])
        cv2.imshow('image_stacked',img)
        cv2.waitKey(0)
    else:
        return('check the dimensions')


#stacking(imgArray,[3,3],0.2)
'''
img = imgArray[0]

image = cv2.imread(img)
image  = cv2.resize(image,(256,256))
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray  = cv2.cvtColor(gray_image,cv2.COLOR_GRAY2BGR)
im = cv2.hconcat([image,gray])
cv2.imshow('stack',im)
cv2.waitKey(0)

'''