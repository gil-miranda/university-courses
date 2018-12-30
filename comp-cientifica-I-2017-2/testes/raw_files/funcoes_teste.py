import numpy as np

def g1(x):
    return np.exp(x) - 2

def g2(x):
    return x**2 - 2

def g3(x):
    return np.sin(x) - np.cos(x**2)

def g4_gen(y):
    def g4(x):
        return x**5 + x*y + 1
    return g4

def g5_gen(a,b):
    def g5(x):
        return a + np.log(x+b)
    return g5
