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
        df = pd.read_csv(f'evolve_{i:.1f}_{metal}', delim_whitespace=True)
        df.columns = ['C1', 'Star Type', 'C3', 'Mass [Sun Mass]', 'C5', 'Radius [Log10]', 'C7', 'C8', 'C9', 'C10', 'C11']
        '''
        Finding max radius
        '''
        max_row = df[df['Radius [Log10]'] == df['Radius [Log10]'].max()]


        max_radius = max_row['Radius [Log10]'].values[0]

    
        '''
        Finding max radius in main sequence
        '''
        if((i <= 0.6 and metal == 0.001) or (i <= 0.7 and metal == 0.02)):
            filtered_df = df[df['Star Type'] == 0]
        else:
            filtered_df = df[df['Star Type'] == 1]
        max_row_ms = filtered_df[filtered_df['Radius [Log10]'] == filtered_df['Radius [Log10]'].max()]
        max_radius_ms = max_row_ms['Radius [Log10]'].values[0]

        

        Rgen[n] = (metal, i, max_radius)
        Rms[n] = (metal, i, max_radius_ms)
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






#HR Diagram part
f = open("evolve_2.0_0.001", "r")
data1 = f.readlines()[1:]
f.close()
teff1 = np.zeros(len(data1))
l1 = np.zeros(len(data1))
i = 0
typ1 = np.zeros(len(data1))
for x in data1:
    teff1[i] = x.split()[6]
    l1[i] = x.split()[4]
    typ1[i] = x.split()[1]
    i += 1

f = open("evolve_6.0_0.02", "r")
data2 = f.readlines()[1:]
f.close()
teff2 = np.zeros(len(data2))
l2 = np.zeros(len(data2))
i = 0
typ2 = np.zeros(len(data2))
for x in data2:
    teff2[i] = x.split()[6]
    l2[i] = x.split()[4]
    typ2[i] = x.split()[1]
    i += 1



#Plot map for HR diagram
type_colors = {
    0: 'violet',
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

cmap = ListedColormap([type_colors[type_val] for type_val in typ1])
unique_types = np.unique(typ1)
legend_elemts = [Line2D([0], [0], marker='o', color='w', label=f'{i}', markerfacecolor=type_colors[i], markersize=5)
                 for i in unique_types]


plt.figure('HR diagram')
plt.scatter(teff1,l1, s=2, c=typ1, cmap=cmap)
plt.text(4.09, 1.4, 'M = 2 \n z = 0.001', fontsize=7, c='black', fontweight='bold')
plt.scatter(teff2,l2, s=2, c=typ2, cmap=cmap)
plt.text(4.28, 3, 'M = 6 \n z = 0.02', fontsize=7, c='black', fontweight='bold')
plt.xticks(np.arange(3,5.5,0.25))
plt.yticks(np.arange(-5.5, 5, 0.5))
plt.xlim(5.5,3)
plt.ylim(-5.6, 5)
plt.xlabel('Effective Temperature (log10) [K]')
plt.ylabel('Effective Luminosity (log10) [Sun Luminosity]')
plt.legend(handles=legend_elemts, title='Star Types')


type_colors_2 = {
    0.001: 'red',
    0.02: 'blue',
}

cmap2 = ListedColormap([type_colors_2[val] for val in Rms[:,0]])
legend_labels_ms = [plt.Line2D([0], [0], marker='o', color='w', label=key, markerfacecolor=value)
                 for key, value in type_colors_2.items()]

plt.figure('Main Sequence Max Radius-Mass Relation')
plt.scatter(Rms[:,1], Rms[:,2], s=2, c=Rms[:,0], cmap=cmap2)
plt.xlabel('Mass [Sun Mass]')
plt.ylabel('Max Radius [Log10 [Sun Radius]')
plt.title('Max Radius-Mass Relation for Main Sequence')
plt.legend(handles=legend_labels_ms, title='Metalicity')

type_colors_3 = {
    0.001: 'red',
    0.02: 'blue',
}

cmap3 = ListedColormap([type_colors_3[val] for val in Rgen[:,0]])
legend_labels_gen = [plt.Line2D([0], [0], marker='o', color='w', label=key, markerfacecolor=value)
                 for key, value in type_colors_3.items()]


plt.figure('Max Radius-Mass Relation - all types')
plt.scatter(Rgen[:,1], Rgen[:,2], s=2, c=Rgen[:,0], cmap=cmap3)
plt.xlabel('Mass [Sun Masses]')
plt.ylabel('Max Radius [Log10] [Sun Radius]')
plt.title('Max Radius-Mass Relation for the entire evolution process')
plt.legend(handles=legend_labels_gen, title='Metalicity')
plt.show()
