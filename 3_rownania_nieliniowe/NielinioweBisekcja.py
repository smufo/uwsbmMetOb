#metoda bisekcji - zawsze znajdzie wynik, ale powolna
from sympy import sympify, symbols

podanaFunkcja = sympify(input('podaj funkcję np. x**2 - 2'))
a = float(input('podaj początek przedziału'))
b = float(input('podaj koniec przedziału'))
dokl = float(input('podaj dokładności przedziału'))

def wybrana_funkcja(x):
    return podanaFunkcja.subs(symbols('x'), x)

#funkcja musi mieć przeciwne znaki na końcach przedziału
if wybrana_funkcja(a) * wybrana_funkcja(b) > 0:
    print("Błąd...")
    exit()

while (True):
    c = (a + b) / 2 #punkt środkowy
    if abs(c-a) < dokl:
        wynik = c
        break
    if wybrana_funkcja(a) * wybrana_funkcja(c) < 0:
        b = c #miejsce zerowe po lewej
    else:
        a = c #miejsce zerowe po prawej

print(wynik)