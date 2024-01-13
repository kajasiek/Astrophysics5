import numpy as np
import matplotlib.pyplot as plt


# Constants/Initial values
M10 = 2 #Msun
M20 = 1 #Msun
A0 = 10 #R0
q0 = M10/M20

RL0 = 2/3**(4/3) * (1 + q0)**(-1/3) * A0
tNE1 = (10)/M10**2
tNE2 = (10)/M20**2

RTE = 0.8

R01 = M10**0.8 #in Rsun
R02 = M20**0.8 #in Rsun

Mj = 0.2 * M10
Rj = 0.3 * R01

V0 = 4/3 * np.pi * R01**3 - 4/3 * np.pi * Rj**3
rhoot0 = (M10 - Mj)/V0 #Msun/Rsun

dt = 0.001 * tNE1

t = 0
M1 = M10
M2 = M20
RL = RL0
rhoot = rhoot0
V = V0
for i in range(1000):

    Rlog1 = np.log10(R01) + RTE * np.log10(M1/M10) + t/tNE1
    Rlog2 = np.log10(R02) + RTE * np.log10(M2/M20) + t/tNE2
    V = 4/3 * np.pi * ((10**Rlog1)**3 - Rj**3)

    rhoot = (M1 - Mj)/V
    if(10**Rlog1 > RL): # New values of: M1, M2, q, RL, A
        dM = rhoot * 4/3 * np.pi * ((10**Rlog1)**3 - RL**3)
        M1 = M1 - dM
        M2 = M2 + dM
        if(M1 < Mj):
            break
        q = M1/M2
        A = A0 * (M20/M2)**2 * (M10/M1)**2
        RL = 2/3**(4/3) * (1 + q)**(-1/3) * A
        #plt.scatter(t, dM)
    plt.scatter(M1, 10**Rlog1, c='b')
    plt.scatter(M1, 10**Rlog2, c='r')
    plt.scatter(M1, RL, c='g')
    #plt.scatter(t, M1, c='b')
    #plt.scatter(t, M2, c='r')

    t += dt
plt.xlabel('M1')
plt.ylabel('R [Rsun]')
plt.legend()
plt.show()
