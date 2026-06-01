import random
import time

random.seed()
def objetosc_hiperkuli(n, liczba_losowan):
    trafienia = 0

    for i in range(liczba_losowan):
        suma_kwadratow = sum((random.uniform(-1.0, 1.0)) ** 2 for _ in range(n))
        if suma_kwadratow <= 1.0:
            trafienia += 1

    objetosc_kostki = 2 ** n
    estymowana_objetosc = (trafienia / liczba_losowan) * objetosc_kostki
    efektywnosc_procent = (trafienia / liczba_losowan) * 100

    return estymowana_objetosc, efektywnosc_procent

wymiary_do_testow = [2, 3, 5, 10]
liczba_losowan = 1000000

print(f"Liczba losowań na wymiar: {liczba_losowan}\n")

for n in wymiary_do_testow:
    start = time.time()
    obj, efekt = objetosc_hiperkuli(n, liczba_losowan)
    czas = time.time() - start

    print(f"Wymiar (n) = {n}")
    print(f"  Estymowana objętość: {obj}")
    print(f"  Efektywność losowań: {efekt} % trafień")
    print(f"  Czas obliczeń:       {czas} s")
    print("--------------------------------------------")