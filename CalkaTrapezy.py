from sympy import sympify, symbols

podanaFunkcja = sympify(input('podaj funkcję np. x**2 - 2'))
a = float(input('podaj początek przedziału całkowania'))
b = float(input('podaj koniec przedziału całkowania'))
n = int(input('podaj liczbę podprzedziałów'))

def wybrana_funkcja(x):
    return podanaFunkcja.subs(symbols('x'), x)

szerokosc_przedzialu = (b - a) / n
h = szerokosc_przedzialu

suma = 0

for i in range(n):
    xi = a + i * h
    xi_1 = a + (i + 1) * h
    pole = ((wybrana_funkcja(xi) + wybrana_funkcja(xi_1)) / 2) * h
    suma += pole

print('Wynik całki metodą trapezów:', suma)