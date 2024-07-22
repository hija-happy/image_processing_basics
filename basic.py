import cv2
from matplotlib import pyplot as plt

#####################
#1. load the image
#################
image = cv2.imread('C:/Users/hijah/Pictures/WE4/WIN_20240625_15_57_16_Pro.jpg')  #give the path of the image

#display the image
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#convert bgr to rgb for matplotlib
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#display the image using matplotlib
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

#####################
#2. grayscale conversion
#################


gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image,cmap='gray')
plt.axis('off')
plt.show()

#####################
#3. image resize
#################

resized_image = cv2.resize(image,(100,100)) #get resized to 100x100 pixels
plt.imshow(cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()