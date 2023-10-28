import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import tplquad


ratio = np.arange(0.01, 100, 0.1)



plt.title("Hill/Roche sphere radius")
plt.xlabel("q")
plt.ylabel("RL")
plt.text(20, 0.65, "Calculated manually", c='b')
plt.text(20, 0.48, "Paczynski approximation", c='r')
plt.text(20, 0.23, "Kopal approximation", c='g')
for i, q in enumerate(ratio):
    A = 2 * (1 + q)
    B = - 4 * (1 + q)/(1 - q) + 4 * q 
    C = 2 * (1 + q)/(1 - q)**2 + 8 * q/(1 - q) + 2 * q**2/(1 + q)
    D = 4 * q/(1 - q)**2 + 4 * q**2/(1 - q**2) - q + 1
    E = 2 * q**2/((1 + q) * (1 - q)**2) - 2 * q**2/(1 + q) - 2/(1 - q)
    F = - q**3/(1 + q)**2 + 1/(1 - q)**2
    



    sol = np.roots([A,B,C,D,E,F])

    
    x1 = -1/(1+q)
    x2 = q/(1+q)
    
    R = np.abs((sol[2] - x1))
    
    f = lambda z, y, x: 1
    
    volume = tplquad(f, x1-R, sol[2], -R, R, -R, R)
    rl = ((3 * volume[0])/(4 * np.pi))**(1/3)
    plt.scatter(q, rl, c='b', s=5)

rl1 = 2/3**(4/3) * (ratio/(1+ratio))**(1/3)
rl2 = 2/3**(4/3) * (1+ratio)**(-1/3)
plt.scatter(ratio, rl1, c='r', s=5)
plt.scatter(ratio, rl2, c='g', s=5)
plt.show()