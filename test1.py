import numpy as np
import math


class Neuron:

    def __init__(self, w):

        self.w = w


    def y(self, x):

        s = np.dot(self.w, x)
        return s


    def onestep(x):

        step = 5
        if x >= step:            
            return 1
        else:            
            return 0


    def sigmoid(x):

        return 1 / (1 + np.exp(0.25 * (-x)))

        




Xi = np.array([1, 1, 1, 1])
Wi = np.array([5, 4, 1, 1])

n = Neuron(Wi)
print('S1 = ', n.y(Xi))
print('Result ', Neuron.onestep(n.y(Xi)))
print('Result ', Neuron.sigmoid(n.y(Xi)))    


Xi = np.array([0, 0, 0, 1])
print('S1 = ', n.y(Xi))
print('Result ', Neuron.onestep(n.y(Xi)))    
print('Result ', Neuron.sigmoid(n.y(Xi)))    

