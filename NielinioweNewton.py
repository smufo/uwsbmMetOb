from sympy import sympify, symbols, diff
x = symbols('x')

podanaFunkcja = sympify(input('podaj funkcję np. x**2 - 2'))
pochodna = diff(podanaFunkcja, x)

xn = float(input('podaj punkt poczatkowy xn'))
epsilon = float(input('podaj tolerancje bledu'))

while True:
    yDlaXn = float(podanaFunkcja.subs(x, xn))
    if abs(yDlaXn) < epsilon:
        break
    xn = xn - podanaFunkcja.subs(x, xn) / pochodna.subs(x, xn)

print('Rozwiązaniem z dokładnością do', epsilon, 'jest xn = ', xn)