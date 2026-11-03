import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 50)
y = x**2

#plt.plot(x, y)
#plt.show()

# NACA 2412

t = 0.12
m = 0.02
p = 0.4

yt = 5*t*(0.2969*np.sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)
yb = yt*-1

#ycf = np.where(x < p, (m/p**2)*(2*p*x-x**2))
#ycb = np.where(x >= p, ((m/(1-p)**2)*1-2*p+2*p*x-x**2))

yc = np.where(x >= p, ((m/(1-p)**2)*(1-2*p+2*p*x-x**2)), ((m/p**2)*(2*p*x-x**2)))

print(yt.max())
print(yc.max())

plt.plot(x, yt)
plt.plot(x, yb)
plt.plot(x, yc)

plt.axis("equal")

plt.show()
