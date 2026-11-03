import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 50)

# example: NACA 2412

#t = 0.12
#m = 0.02
#p = 0.4

naca = input("Enter a 4-digit NACA number:")

# t = thickness
t = int(naca[2:4])/100
# m = maximum camber
m = int(naca[0])/100
# p = position of camber
p = int(naca[1])/10

yt = 5*t*(0.2969*np.sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)

if p == 0:
    yc = np.zeros_like(x)
else:
    yc = np.where(x >= p, ((m/(1-p)**2)*(1-2*p+2*p*x-x**2)), ((m/p**2)*(2*p*x-x**2)))

yu = yt + yc
yl = yc - yt

plt.plot(x, yu, label = "upper surface")
plt.plot(x, yl, label = "lower surface")
plt.plot(x, yc, ls='--', label="camber")

plt.axis("equal")
plt.legend()
plt.grid()
plt.title("NACA " + naca + " Airfoil")
plt.xlabel("Chord")
plt.ylabel("Thickness")

plt.show()
