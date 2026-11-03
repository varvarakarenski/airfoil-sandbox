import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 50)

# NACA 2412

t = 0.12
m = 0.02
p = 0.4

yt = 5*t*(0.2969*np.sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)

yc = np.where(x >= p, ((m/(1-p)**2)*(1-2*p+2*p*x-x**2)), ((m/p**2)*(2*p*x-x**2)))

yu = yt + yc
yl = yc - yt

plt.plot(x, yu)
plt.plot(x, yl)
plt.plot(x, yc)

plt.axis("equal")

plt.show()
