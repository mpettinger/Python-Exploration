import numpy as np

ones_array = np.random.randint(100,size = (10,5,5))

def cond(array):
    return np.greater(array,5)
mean = np.mean(ones_array,axis = 0)
print(f"""The mean is
{mean} """)
