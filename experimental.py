import numpy as np
import matplotlib.pyplot as plt

image = np.reshape(np.arange(5*5*3),(5,5,3))

redlayer = np.reshape(np.arange(5*5),(5,5))
redlayer.fill(128)

image[0:5,0:5,0] = redlayer
image[3,3,1] = 256
image[0:5,0:5,2] = redlayer

print(image)
plt.imshow(image)
plt.show()