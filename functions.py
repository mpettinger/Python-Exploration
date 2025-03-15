import numpy as np

x_values = np.array([0,1,2,3,4,5,6,7,8,9,10], dtype='float32')

def linear(x):
    return 1.5*x + 3

def summing(f, data):
    ys = f(data)
    return ys.sum()

print(f"{summing(linear,x_values)}")