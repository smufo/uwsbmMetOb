import random
import math
random.seed()

def oblicz_pi(liczba_losowan):
    wyniki = []
    for i in range(liczba_losowan):
        x = random.random()
        y = random.random()

        if x ** 2 + y ** 2 <= 1.0:
            wyniki.append(4.0)
        else:
            wyniki.append(0.0)

    estymator = sum(wyniki) / liczba_losowan

    suma_kwadratow_odchylen = sum((x - estymator) ** 2 for x in wyniki)
    wariancja = suma_kwadratow_odchylen / (liczba_losowan - 1)

    blad_std = math.sqrt(wariancja / liczba_losowan)

    return estymator, wariancja, blad_std

pi_estymowane, wariancja, blad_std = oblicz_pi(5000000)
print(f"Wartość PI wynosi: {pi_estymowane}")
print(f"Wariancja z próby wynosi: {wariancja}")
print(f"Błąd standardowy wynosi: {blad_std}")