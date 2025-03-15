"""
This scrpit is to practice taking arrays and combining them into different shapes
"""

import numpy as np

array1 = np.reshape(np.arange(75),(5,5,3))
array2 = np.reshape(np.arange(75),(5,5,3))
array3 = np.reshape(np.arange(75),(5,5,3))
array4 = np.reshape(np.arange(75),(5,5,3))
combined = np.stack((array1,array2,array3,array4))
print(f"""array1 is:
{array1}

array2 is
{array2}

Combined array is \n{combined.shape}""")