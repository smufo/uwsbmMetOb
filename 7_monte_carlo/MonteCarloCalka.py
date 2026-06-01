import random
import math

random.seed()
def calka_monte_carlo(funkcja, a, b, liczba_losowan):
    suma_f = 0.0
    suma_f_kwadrat = 0.0
    for i in range(liczba_losowan):
        x = a + (b - a) * random.random()
        y = funkcja(x)
        suma_f += y
        suma_f_kwadrat += y ** 2

    srednia_f = suma_f / liczba_losowan
    estymator = (b - a) * srednia_f
    wariancja_f = (suma_f_kwadrat - liczba_losowan * (srednia_f ** 2)) / (liczba_losowan - 1)
    blad_std = (b - a) * math.sqrt(wariancja_f / liczba_losowan)

    return estymator, wariancja_f, blad_std

def badana_funkcja(x):
    return (x ** 2) * math.sin(x ** 3)

dolna_granica = 0.0
gorna_granica = 2.0
N = 1000000
wartosc_analityczna = 0.381831

wynik_calki, wariancja, blad = calka_monte_carlo(badana_funkcja, dolna_granica, gorna_granica, N)

print(f"Badany przedział: [{dolna_granica}, {gorna_granica}]")
print(f"Liczba losowań (N): {N}")
print(f"Wynik estymowany: {wynik_calki}")
print(f"Wynik analityczny: {wartosc_analityczna}")
print(f"Błąd bezwzględny: {abs(wynik_calki - wartosc_analityczna)}")
print(f"Wariancja z próby: {wariancja}")
print(f"Błąd standardowy metody: {blad}")