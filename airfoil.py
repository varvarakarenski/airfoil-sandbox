import matplotlib
matplotlib.use("agg")  # workers have no DOM canvas; render to an image instead
import matplotlib.pyplot as plt
import numpy as np
from pyscript import display, document, when # type: ignore

# example: NACA 2412

#t = 0.12
#m = 0.02
#p = 0.4

beta = np.linspace(0, np.pi, 200)
x = (1-np.cos(beta))/2
current_tail = "no"

def naca4(m, p, t, tail):

    if tail == "yes":
        yt = 5*t*(0.2969*np.sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1036*x**4)
    elif tail == "no":
        yt = 5*t*(0.2969*np.sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)

    if m == 0:
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

def draw_plot():
    t = float(document.getElementById("t-slider").value)
    m = float(document.getElementById("m-slider").value)
    p = float(document.getElementById("p-slider").value)

    document.getElementById("t-val").innerText = f"{t:.2f}"
    document.getElementById("m-val").innerText = f"{m:.2f}"
    document.getElementById("p-val").innerText = f"{p:.1f}"
    
    xu, yu, xl, yl, yc = naca4(m, p, t, current_tail)
    code = f"{round(m * 100)}{round(p * 10)}{round(t * 100):02d}"

    fig, ax = plt.subplots(figsize=(8,4))

    ax.plot(xu, yu, label="upper surface")
    ax.plot(xl, yl, label="lower surface")
    ax.plot(x, yc, ls='--', label="camber")

    ax.axis("equal")
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
    ax.grid()
    ax.set_title("NACA " + code + " Airfoil")
    ax.set_xlabel("Chord")
    ax.set_ylabel("Thickness")
    fig.tight_layout()

    document.getElementById("plot-area").innerHTML = ""
    display(fig, target="plot-area")
    plt.close(fig)

def start_airfoil_plot(naca, tail):
    global current_tail
    current_tail = tail

    # t = thickness
    t = int(naca[2:4])/100
    # m = maximum camber
    m = int(naca[0])/100
    # p = position of camber
    p = int(naca[1])/10

    if p == 0:
        p = 0.4

    document.getElementById("t-slider").value = str(t)
    document.getElementById("m-slider").value = str(m)
    document.getElementById("p-slider").value = str(p)

    document.getElementById("plotter-section").style.display = "block"
    draw_plot()

naca = input("Enter a 4-digit NACA number: ")

while not naca.isdigit() or len(naca) != 4:
    naca = input("Please enter a 4-digit NACA number: ")

tail = input("Simulate a closed tail? (yes/no) ")

while tail != "yes" and tail != "no":
    tail = input("Please answer with a lowercase 'yes' or 'no'. Computers don't have very good imaginations. ")

start_airfoil_plot(naca, tail)

@when("input", "#t-slider")
@when("input", "#m-slider")
@when("input", "#p-slider")
def on_slider_change(event):
    draw_plot()
