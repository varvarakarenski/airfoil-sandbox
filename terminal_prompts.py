from pyscript import window # type: ignore

naca = input("Enter a 4-digit NACA number: ")

while not naca.isdigit() or len(naca) != 4:
    naca = input("Please enter a 4-digit NACA number: ")

tail = input("Simulate a closed tail? (yes/no) ")

while tail != "yes" and tail != "no":
    tail = input("Please answer with a lowercase 'yes' or 'no'. Computers don't have very good imaginations. ")

window.startAirfoilPlot(naca, tail)