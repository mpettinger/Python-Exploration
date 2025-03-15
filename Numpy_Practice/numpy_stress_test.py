import numpy as np
imagex = 100
imagey = 100
first_array = np.reshape(np.ones((imagex,imagey),dtype = np.int8),((imagex*imagey),1))

second_array = np.ones((10000,(imagex*imagey)),dtype=np.int8)

print(f"""The shape of first_array is {first_array.shape}
The shape of second_array is {second_array.shape}""")

array_product = second_array @ first_array

print(f"The shape of array_product is {array_product.shape} and data type is {array_product.dtype}")