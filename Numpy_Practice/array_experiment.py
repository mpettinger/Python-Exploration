import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import numpy as np
red,green,blue,alpha = (0,0,0,255)
length = 255
width = 255

red_layer = np.full((width,length),red,dtype=np.uint8)
green_layer = np.full((width,length),green,dtype=np.uint8)
blue_layer = np.full((width,length),blue,dtype=np.uint8)
alpha_layer = np.full((width,length),alpha,dtype=np.uint8)

generated_image = np.stack((red_layer,green_layer,blue_layer,alpha_layer),axis = 2)
shape = (width,50)
#position one
generated_image[:,00:50,1] = np.full(shape,255,dtype=np.uint8)
#position two
generated_image[:,51:101,2] = np.full(shape,255,dtype=np.uint8)
#position three (middle)
generated_image[:,102:152,0] = np.full(shape,255,dtype=np.uint8)
#position four
generated_image[:,153:203,0] = np.full(shape,255,dtype=np.uint8)
generated_image[:,153:203,1] = np.full(shape,255,dtype=np.uint8)
generated_image[:,153:203,2] = np.full(shape,0,dtype=np.uint8)

#positon five (end)
generated_image[:,204:254,0] = np.full(shape,255,dtype=np.uint8)
generated_image[:,204:254,1] = np.full(shape,255,dtype=np.uint8)
generated_image[:,204:254,2] = np.full(shape,255,dtype=np.uint8)
#image_array = np.array(image)
print(f"The array shape is: {generated_image.shape}")

#print(f"Array values of top slice is {first_layer}")

plt.imshow(generated_image)
plt.show()