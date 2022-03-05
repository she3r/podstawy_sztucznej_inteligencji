import pandas as pd
import seaborn as sns
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

url = r'http://jse.amstat.org/datasets/babyboom.dat.txt'
data = pd.read_csv(url, delimiter='[ ]+', header=None, engine='python', names=['sex', 'Weight', 'Minutes'])

male = data[data.sex == 1]
female = data[data.sex == 2]
f_fig, f_axes = plt.subplots(3, 2)
m_fig, m_axes = plt.subplots(3, 2)
maleWeight = male.Weight.values
femaleWeight = female.Weight.values
# wykres w ksztalcie szeregu czasowego
m_axes[0][0].scatter(np.arange(len(maleWeight)), maleWeight)
f_axes[0][0].scatter(np.arange(len(femaleWeight)), femaleWeight)
m_axes[0][0].set_title('szereg czasowy', fontsize=7.5)
f_axes[0][0].set_title('szereg czasowy', fontsize=7.5)

# estymacje gestosci
sns.kdeplot(maleWeight,ax=m_axes[0][1])
sns.kdeplot(femaleWeight,ax=f_axes[0][1])
f_axes[0][1].set_title('est. gestosci', fontsize=7.5)
m_axes[0][1].set_title('est. gestosci', fontsize=7.5)

# histogramy
m_axes[1][0].hist(maleWeight, bins=10)
f_axes[1][0].hist(femaleWeight, bins=10)
m_axes[1][0].set_title('histogram', y=1.0, pad=-14, fontsize=7.5)
f_axes[1][0].set_title('histogram', y=1.0, pad=-14, fontsize=7.5)

# wykresy skrzypcowe
sns.violinplot(maleWeight, ax=m_axes[1][1])
sns.violinplot(femaleWeight, ax=f_axes[1][1])

# dystrybuanty empiryczne
m_axes[2][0].plot(sp.stats.cumfreq(maleWeight, numbins=20)[0])
f_axes[2][0].plot(sp.stats.cumfreq(femaleWeight, numbins=20)[0])
m_axes[2][0].set_title('dystryb. emp.', y=1.0, pad=-14, fontsize=7.5)
f_axes[2][0].set_title('dystryb. emp.', y=1.0, pad=-14, fontsize=7.5)

# wykresy pudelkowe
m_axes[2][1].boxplot(maleWeight, sym='.')
f_axes[2][1].boxplot(femaleWeight, sym='.')

# tytuly opracowan
m_fig.suptitle('Male', fontsize=16)
f_fig.suptitle('Female', fontsize=16)
m_fig.tight_layout()
f_fig.tight_layout()
for axes in (m_axes,f_axes):
    for w in axes:
        for ax in w:
            # ax.xaxis.set_visible(False)
            ax.yaxis.set_visible(False)


plt.show()