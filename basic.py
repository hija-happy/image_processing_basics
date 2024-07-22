import cv2
from matplotlib import pyplot as plt

#####################
#load the image
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
plt.show()