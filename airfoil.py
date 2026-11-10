import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider

# example: NACA 2412

#t = 0.12
#m = 0.02
#p = 0.4

beta = np.linspace(0, np.pi, 200)
x = (1-np.cos(beta))/2

a = 1

def naca4(m, p, t, tail):

    if tail == "yes":
        yt = 5*t*(0.2969*np.sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1036*x**4)
    elif tail == "no":
        yt = 5*t*(0.2969*np.sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)

    if p == 0:
        yc = np.zeros_like(x)
        dyc = np.zeros_like(x)
    else:
        yc = np.where(x >= p, ((m/(1-p)**2)*(1-2*p+2*p*x-x**2)), ((m/p**2)*(2*p*x-x**2)))
        dyc = np.where(x >= p, ((2*m)/(1-p)**2)*(p-x), ((2*m)/p**2)*(p-x))

    theta = np.arctan(dyc)

    xu = x-yt*np.sin(theta)
    yu = yc+yt*np.cos(theta)

    xl = x+yt*np.sin(theta)
    yl = yc-yt*np.cos(theta)

    return xu, yu, xl, yl, yc

naca = input("Enter a 4-digit NACA number: ")

while not naca.isdigit() or len(naca) != 4:
    naca = input("Please enter a 4-digit NACA number: ")

tail = input("Simulate a closed tail? (yes/no) ")

while tail != "yes" and tail != "no":
    tail = input("Please answer with a lowercase 'yes' or 'no'. Computers don't have very good imaginations. ")

# t = thickness
t = int(naca[2:4])/100
# m = maximum camber
m = int(naca[0])/100
# p = position of camber
p = int(naca[1])/10

xu, yu, xl, yl, yc = naca4(m, p, t, tail)

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.25, bottom=0.25)
thickness_ax = fig.add_axes((0.25, 0.1, 0.65, 0.03))

upper_line, = ax.plot(xu, yu, label="upper surface")
lower_line, = ax.plot(xl, yl, label="lower surface")
camber_line, = ax.plot(x, yc, ls='--', label="camber")

thickness_slider = Slider(
    ax=thickness_ax,
    label='Thickness',
    valmin=0.01,
    valmax=0.5,
    valinit=t,
)

def update(val):
    xu, yu, xl, yl, yc = naca4(m, p, thickness_slider.val, tail)
    upper_line.set_data(xu, yu)
    lower_line.set_data(xl, yl)
    camber_line.set_data(x, yc)
    fig.canvas.draw_idle(x, yc)

thickness_slider.on_changed(update)

ax.axis("equal")
ax.legend()
ax.grid()
ax.set_title("NACA " + naca + " Airfoil")
ax.set_xlabel("Chord")
ax.set_ylabel("Thickness")

plt.show()
