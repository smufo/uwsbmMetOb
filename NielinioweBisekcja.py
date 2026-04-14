from sympy import sympify, symbols

a = float(input('podaj początek przedziału'))
b = float(input('podaj koniec przedziału'))
dokl = float(input('podaj dokładności przedziału'))
podanaFunkcja = sympify(input('podaj funkcję np. x**2 - 2'))

def wybrana_funkcja(x):
    return podanaFunkcja.subs(symbols('x'), x)

if wybrana_funkcja(a) * wybrana_funkcja(b) > 0:
    print("Błąd...")
    exit()

while (True):
    c = (a + b) / 2
    if abs(c-a) < dokl:
        wynik = c
        break
    if wybrana_funkcja(a) * wybrana_funkcja(c) < 0:
        b = c
    else:
        a = c

print(wynik)