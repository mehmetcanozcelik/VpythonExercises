import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')

plt.rcParams['font.size'] = 18

x0=0
y0=0
x = 0
y = 0 
L1 = []
L2 = []

for i in range(0,1000000) :
    x0 = x
    y0 = y
    randomnum = np.random.randint(0,100)
    if (randomnum >0 and randomnum <85):
        x = x0*(0.85) + y0*(0.04)
        y = x0*(-0.04) + y0*(0.85) + 1.6
        L1.append(x)
        L2.append(y)

    elif (randomnum >=85 and randomnum <92):
        x = x0*(0.2) + y0*(-0.26)
        y = x0*(0.23) + y0*(0.22) + 1.6
        L1.append(x)
        L2.append(y)

    elif (randomnum >=92 and randomnum <100):
        x = x0*(-0.15) + y0*(0.28)
        y = x0*(0.26) + y0*(0.24) + 0.44
        L1.append(x)
        L2.append(y)

    elif (randomnum ==0):
        x = 0
        y = y0*(0.16)
        L1.append(x)
        L2.append(y)

plt.plot(L1, L2, ',', color = 'purple' , ms=5)
# plt.savefig('fractal.png', format='png', dpi=400)
#plt.axis([0,1,4,6])
plt.show()
