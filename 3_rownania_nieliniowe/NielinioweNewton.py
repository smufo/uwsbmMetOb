from sympy import sympify, symbols, diff
x = symbols('x')

podanaFunkcja = sympify(input('podaj funkcję np. x**2 - 2'))
pochodna = diff(podanaFunkcja, x)
xn = float(input('podaj punkt poczatkowy xn'))
epsilon = float(input('podaj tolerancje bledu'))

def wybrana_funkcja(x):
    return podanaFunkcja.subs(symbols('x'), x)

while True:
    yDlaXn = float(wybrana_funkcja(xn))
    if abs(yDlaXn) < epsilon:
        break
    xn = xn - podanaFunkcja.subs(x, xn) / pochodna.subs(x, xn)

print('Rozwiązaniem z dokładnością do', epsilon, 'jest xn = ', xn)