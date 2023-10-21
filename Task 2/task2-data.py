import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D
import pandas as pd






#Max R during main sequence and max R in general
z = [0.001, 0.02]
Rgen = np.zeros([70,3])
Rms = np.zeros([70,3])

n = 0

for metal in z:
    i = 0.1 #Add a loop here
    while(i < 100.02):
        print(f'evolve_{i}_{metal}')
        df = pd.read_csv(f'evolve_{i:.1f}_{metal}', delim_whitespace=True)
        df.columns = ['C1', 'Star Type', 'C3', 'Mass [Sun Mass]', 'C5', 'Radius [Log10]', 'C7', 'C8', 'C9', 'C10', 'C11']
        '''
        Finding max radius
        '''
        max_row = df[df['Radius [Log10]'] == df['Radius [Log10]'].max()]


        max_radius = max_row['Radius [Log10]'].values[0]
        typ = max_row['Star Type'].values[0]
        mass = max_row['Mass [Sun Mass]'].values[0]
    
        '''
        Finding max radius in main sequence
        '''
        if((i <= 0.6 and metal == 0.001) or (i <= 0.7 and metal == 0.02)):
            filtered_df = df[df['Star Type'] == 0]
        else:
            filtered_df = df[df['Star Type'] == 1]
        max_row_ms = filtered_df[filtered_df['Radius [Log10]'] == filtered_df['Radius [Log10]'].max()]
        max_radius_ms = max_row_ms['Radius [Log10]'].values[0]
        type_ms = max_row_ms['Star Type'].values[0]
        mass_ms = max_row_ms['Mass [Sun Mass]'].values[0]
        

        Rgen[n] = (typ, mass, max_radius)
        Rms[n] = (type_ms, mass_ms, max_radius_ms)
        n += 1
        if(i < 0.99):
            i += 0.1
        elif(i < 9.99):
            i += 1
        elif(i < 24.99):
            i += 2.5
        elif(i < 49.99):
            i += 5
        else:
            i += 10


print(Rgen)
print(Rms)


#HR Diagram part
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





#Plot map for HR diagram
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
