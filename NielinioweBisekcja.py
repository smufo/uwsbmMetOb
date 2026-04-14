from sympy import sympify, symbols

a = float(input('podaj poczatek przedzialu'))
b = float(input('podaj koniec przedzialu'))
dokl = float(input('podaj dokladnosc przedzialu'))
podanaFunkcja = sympify(input('podaj funkcje np. x**2 - 2'))

def wybranaFunkcja(x):
    return podanaFunkcja.subs(symbols('x'), x)

if wybranaFunkcja(a) * wybranaFunkcja(b) > 0:
    print("Błąd...")
    exit()

while (True):
    c = (a + b) / 2
    if abs(c-a) < dokl:
        wynik = c
        break
    if wybranaFunkcja(a) * wybranaFunkcja(c) < 0:
        b = c
    else:
        a = c

print(wynik)