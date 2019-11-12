import os
import numpy as np
import matplotlib.pyplot as plt

omega = 0.01
delT = 0.1/omega
x = np.linspace (0,4/omega,40)

plt.figure()
data = np.loadtxt("data.dat")
n = len(data)
plt.plot(x, data[0:int(n/2)])
plt.title('Integral_implicita')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("datos.png")
