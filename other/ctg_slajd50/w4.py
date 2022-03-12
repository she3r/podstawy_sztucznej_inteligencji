# centralne twierdzenie graniczne- zadanie z ostatniego slajdu
import matplotlib.pyplot as plt
import numpy as np

N = 10000


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey='row')
sample_uniform = np.random.uniform(low=0, high=20, size=N)
ax1.hist(sample_uniform, bins=50)
ax1.set_title('random data')
average2 = []
average10 = []
x = np.linspace(0,1,num=100)
n, p = 10, 0.5
for q in sample_uniform.astype(int):
    if q >= 2:
        sample_binomial = np.random.binomial(n, p, size=q)
        m = np.mean(sample_binomial)/10
        if q >= 10:
            average10.append(m)

        average2.append(m)

ax2.hist(average2, bins=x)
ax2.set_title('>=2')
ax3.hist(average10, bins=x)
ax3.set_title('>=10')
plt.show()


