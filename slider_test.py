import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

a = 1
x = np.linspace(0, 200)

def f(a, x):
    return a * x**2

fig, ax = plt.subplots()
line, = ax.plot(x, f(a, x), lw=2)
ax.set_xlabel('X whatever')

fig.subplots_adjust(left=0.25, bottom=0.25)

axfreq = fig.add_axes((0.25, 0.1, 0.65, 0.03))
a_slider = Slider(
    ax=axfreq,
    label='a value',
    valmin=0.1,
    valmax=30,
    valinit=a,
)

def update(val):
    line.set_ydata(f(a_slider.val, x))
    fig.canvas.draw_idle()

a_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes((0.8, 0.025, 0.1, 0.04))
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    a_slider.reset()
button.on_clicked(reset)

ax.set_label('a(x)^2')
plt.show()
