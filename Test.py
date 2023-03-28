import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
    return np.array(x>0,dtype=np.int32)



def sigmoid(x):
    return 1/(1+np.exp(-x))

if __name__ == '__main__':
    x=np.array([[1,2,3,5]])
    y=np.array([[5,6,3],[7,8,6],[9,10,11],[12,13,14]])
    print(x.shape)
    print(y.shape)
    print(np.dot(x,y))

