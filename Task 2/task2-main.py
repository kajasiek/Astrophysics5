import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

#HR Diagram for now

f = open("evolve_2.0_0.001", "r")
data = f.readlines()[1:]
f.close()
teff = np.zeros(len(data))
l = np.zeros(len(data))
i = 0
typ = np.zeros(len(data))
for x in data:
    teff[i] = x.split()[6]
    l[i] = x.split()[4]
    typ[i] = x.split()[1]
    i += 1

type_colors = {
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'orange',
    5: 'purple',
    6: 'cyan',
    7: 'magenta',
    8: 'yellow',
    9: 'brown',
    10: 'pink',
    11: 'lime',
}

cmap = ListedColormap([type_colors[type_val] for type_val in typ])
unique_types = np.unique(typ)
legend_elemts = [Line2D([0], [0], marker='o', color='w', label=f'{i}', markerfacecolor=type_colors[i], markersize=5)
                 for i in unique_types]

plt.scatter(teff,l, s=2, c=typ, cmap=cmap)
plt.xticks(np.arange(3,5.5,0.25))
plt.yticks(np.arange(-5.5, 5, 0.5))
plt.xlim(5.5,3)
plt.ylim(-5.6, 5)
plt.xlabel('Effective Temperature (log10) [K]')
plt.ylabel('Effective Luminosity (log10) [Sun Luminosity]')
plt.legend(handles=legend_elemts, title='Star Types')
plt.show()