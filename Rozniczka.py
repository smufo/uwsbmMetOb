from sympy import sympify, symbols
import matplotlib.pyplot as plt

podanaFunkcja = sympify(input('podaj funkcję np. sin(x)'))
a = float(input('podaj początek przedziału'))
b = float(input('podaj koniec przedziału'))
n = int(input('podaj liczbę kroków'))
h = float(input('podaj h (krok różniczkowania)'))

def wybrana_funkcja(x):
    return float(podanaFunkcja.subs(symbols('x'), x))

delta = (b - a) / n

tablica_x = [a + i * delta for i in range(n + 1)]
tablica_y = [wybrana_funkcja(x) for x in tablica_x]
tablica_pochodnych = [(wybrana_funkcja(x + h) - wybrana_funkcja(x - h)) / (2 * h) for x in tablica_x]

plt.plot(tablica_x, tablica_y, marker='.', linestyle='-', color='b', label=str(podanaFunkcja))
plt.plot(tablica_x, tablica_pochodnych, marker='.', linestyle='-', color='r', label='pochodna ' + str(podanaFunkcja))
plt.legend()
plt.grid(True)
plt.xlabel('oś x')
plt.ylabel('oś y')
plt.title('Wykres funkcji oraz jej pochodnej')
plt.show()