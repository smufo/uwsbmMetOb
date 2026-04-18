from sympy import sympify, symbols

podanaFunkcja = sympify(input('podaj funkcję np. x**2 - 2'))
a = float(input('podaj początek przedziału całkowania'))
b = float(input('podaj koniec przedziału całkowania'))
n = int(input('podaj liczbę podprzedziałów (parzysta)'))

while n % 2 != 0:
    n = int(input('liczba podprzedziałów musi być parzysta, podaj jeszcze raz'))

def wybrana_funkcja(x):
    return podanaFunkcja.subs(symbols('x'), x)

h = (b - a) / n
suma = wybrana_funkcja(a) + wybrana_funkcja(b)

for i in range(1, n):
    xi = a + i * h
    if i % 2 == 0:
        suma += 2 * wybrana_funkcja(xi)
    else:
        suma += 4 * wybrana_funkcja(xi)

calka = (h / 3) * suma

print('Wynik całki metodą Simpsona:', calka)