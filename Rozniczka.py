import math
h = float(input('podaj h'))
start = int(input('podaj punkt start'))
end = int(input('podaj punkt end'))
ilekrokow = int(input('podaj liczbe krokow')) - 1
tablica_x = []
tablica_y = []
tablica_pochodnych = []

przedzial = abs(start) + abs(end)
kroczek = przedzial/ilekrokow

tablica_x.append(start)

while len(tablica_x) < ilekrokow:
    tablica_x.append(tablica_x[-1]+kroczek)
tablica_x.append(end)
for x in tablica_x:
    tablica_y.append(math.sin(x))
for x in tablica_x:
    tablica_pochodnych.append((math.sin(x+h) - math.sin(x-h))/(2 * h))

import matplotlib.pyplot as plt
plt.plot(tablica_x, tablica_y, marker='.', linestyle='-', color='b', label='sin(x)')
plt.plot(tablica_x, tablica_pochodnych, marker='.', linestyle='-', color='r', label='podchodna sin(x)')
plt.legend()
plt.grid(True)
plt.xlabel('oś x')
plt.ylabel('oś y')
plt.title('Wykres sin(x) oraz podchodna sin(x)')
plt.show()

