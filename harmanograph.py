import numpy as np
import matplotlib.pyplot as plt

n = 1000000
t = np.logspace(np.log10(150),np.log10(5000),n)

A = [  2, 10, 60, 9 ]
d = [ .004, .001, .002, .0015 ]
f = [   3, 1, 2, 25 ]

x = A[0]*np.sin(t*f[0])*np.exp(-d[0]*t) + A[1]*np.sin(t*f[1])*np.exp(-d[1]*t)
y = A[2]*np.sin(t*f[2])*np.exp(-d[2]*t) + A[3]*np.sin(t*f[3])*np.exp(-d[3]*t)

plt.plot(x,y,'k',linewidth=.1)
plt.axis('off')
plt.show()