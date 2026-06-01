from sympy import sympify, symbols

podanaFunkcja = sympify(input('podaj funkcję np. x**2 - 2'))
a = float(input('podaj początek przedziału całkowania'))
b = float(input('podaj koniec przedziału całkowania'))
n = int(input('podaj liczbę prostokątów'))

def wybrana_funkcja(x):
    return podanaFunkcja.subs(symbols('x'), x)

deltaX = (b - a) / n
suma_pol = 0

for i in range(0, n):
    xi = a + i * deltaX
    hi = wybrana_funkcja(xi)
    suma_pol += hi * deltaX

print('Wynik całki metodą prostokątów:', suma_pol)