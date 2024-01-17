import subprocess
import numpy as np

#Code to automatically run through Binary Star Evolution program created by J. Hurley
#Things to note: This will only work on Linux (wow)

#Constants
G = 2942. #In Rsun^3/(Msun * days^2)

Atable = np.linspace(5., 3000., 25) #In Rsun
m2table = np.linspace(0.5, 20, 25)
m1 = 3.0 #In Msun
m2 = 1. #In Msun
age = 15000. #myr
K1, K2 = 1, 1 #not important, dont change
z = 0.02 #metallicity
e = 0. #eccentricity
for A in Atable:
    for m2 in m2table:
        f = open("binary.in", "r+")
        data = f.readlines()
        P = np.sqrt((A**3 * 4 * np.pi**2)/(G * (m1 + m2)))
        convm1 = str(m1)
        convm2 = str(m2)
        convP = f"{P:.2f}"
        convage = str(age)
        convK1 = str(K1)
        convK2 = str(K2)
        convz = str(z)
        conve = str(e)

        data[0] = convm1 + ' ' + convm2 + ' ' + convage + ' ' + convP + ' ' + convK1 + ' ' + convK2 + ' ' + convz + ' ' + conve + '\n'

        f.seek(0)

        f.writelines(data)

        f.close()
        subprocess.run(["./bse"])
        subprocess.run(["mv", "binary.dat", f"binary_{m2}_{A:.1f}"])