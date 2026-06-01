from sympy import sympify, symbols

podanaFunkcja = sympify(input('podaj funkcję np. x**2 - 2'))
x0 = float(input('Podaj pierwszy punkt startowy x0: '))
x1 = float(input('Podaj drugi punkt startowy x1: '))
epsilon = float(input('Podaj tolerancję błędu: '))

def wybrana_funkcja(x):
    return podanaFunkcja.subs(symbols('x'), x)

while abs(wybrana_funkcja(x1)) > epsilon:
    x0, x1 = x1, x1 - wybrana_funkcja(x1) * (x1 - x0) / (wybrana_funkcja(x1) - wybrana_funkcja(x0))

print('Rozwiązaniem z dokładnością do', epsilon, 'jest x =', x1)