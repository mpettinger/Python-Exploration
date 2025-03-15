import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#/home/pi/Desktop/camerafiles

image = mpimg.imread("/home/pi/Desktop/camerafiles/mikescam1.jpg","r")
image_array = np.array(image)
print(f"The array shape is: {image_array.shape}")

image_slice0 = image_array[:,:,0]
print(f"The first slice is shape {image_slice0.shape}")
plt.subplot(1, 3, 1)
plt.imshow(image_slice0, cmap="Greys")

image_slice1 = image_array[:,:,1]
print(f"The second slice is shape image_slice1 {image_slice1.shape}")
plt.subplot(1, 3, 2)
plt.imshow(image_slice1, cmap="Greys")

image_slice2 = image_array[:,:,2]
print(f"The third slice is shape image_slice1 {image_slice1.shape}")
plt.subplot(1, 3, 3)
plt.imshow(image_slice2, cmap="Greys")

plt.show()
