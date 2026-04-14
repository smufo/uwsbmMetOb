import math
start = float(input('podaj punkt start'))
end = float(input('podaj punkt end'))
ile_przedzialow = int(input('podaj liczbe przedzialow parzysta'))

while ile_przedzialow % 2 != 0:
    ile_przedzialow = int(input('liczba przedzialow musi byc parzysta, podaj jeszcze raz'))

tablica_x = []
tablica_y = []

krok = (end - start) / ile_przedzialow

tablica_x.append(start)

while len(tablica_x) < ile_przedzialow:
    tablica_x.append(tablica_x[-1] + krok)
tablica_x.append(end)

for x in tablica_x:
    tablica_y.append(math.sin(x))

suma = tablica_y[0] + tablica_y[-1]

for i in range(1, len(tablica_y) - 1):
    if i % 2 == 0:
        suma = suma + 2 * tablica_y[i]
    else:
        suma = suma + 4 * tablica_y[i]

calka = (krok / 3) * suma

print('Wynik calki metoda Simpsona:', calka)