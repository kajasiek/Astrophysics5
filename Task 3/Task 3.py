import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import tplquad
from scipy.optimize import root
import sys
import sympy as smp


def ratio(m1, m2):
    q = m2/m1
    if(q > 1):
        print("Wrong values")
        sys.exit()
    else:
        return q

#Constants 
m1 = 2
m2 = 1
q = ratio(m1, m2)

A1 = q/(1+q)
A2 = 1/(1+q)

'''
Finding L1
'''

def phi1l1(x, q):
    return 

def phi1(x, y, z, q):
    return -(1/(1+q))/np.sqrt((x + q/(1+q))**2 + y**2 + z**2)

def phi2(x, y, z, q):
    return -(q/(1+q))/np.sqrt((x - 1/(1+q))**2 + y**2 + z**2) 

def phi3(x, y):
    return -0.5 * (x**2 + y**2) 





fun = lambda z, y, x: 1 
found = tplquad(fun, -1.136, 0.237, -0.8, 0.8, -0.8, 0.8)
print(found)


