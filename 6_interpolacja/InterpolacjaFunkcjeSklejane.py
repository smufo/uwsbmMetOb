wezly_xy = [[1.0, 2.0, 4.0, 5.0, 7.0], [2.0, 4.5, 1.5, 5.0, 3.0]]

x = wezly_xy[0]
y = wezly_xy[1]
n = len(x)

#krok 1 - obliczenie długości przedziałów h_i
h = [x[i + 1] - x[i] for i in range(n - 1)]

#krok 2 - zbudowanie układu równań dla współczynników c_i
A = [[0.0] * n for _ in range(n)]
b = [0.0] * n

#warunki naturalne (c_0 = 0, c_{n-1} = 0)
A[0][0] = 1.0
b[0] = 0.0

A[n - 1][n - 1] = 1.0
b[n - 1] = 0.0

#równania dla punktów wewnętrznych
for i in range(1, n - 1):
    A[i][i - 1] = h[i - 1]
    A[i][i] = 2 * (h[i - 1] + h[i])
    A[i][i + 1] = h[i]
    b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

#krok 3 - rozwiązanie układu trójdiagonalnego metodą Thomasa
def rozwiaz_uklad_trojdiagonalny(A, b):
    n = len(b)

    #eliminacja w przód
    for i in range(1, n):
        wsp = A[i][i - 1] / A[i - 1][i - 1]
        A[i][i] -= wsp * A[i - 1][i]
        b[i] -= wsp * b[i - 1]

    #podstawienie wstecz
    wynik = [0.0] * n
    wynik[n - 1] = b[n - 1] / A[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        wynik[i] = (b[i] - A[i][i + 1] * wynik[i + 1]) / A[i][i]

    return wynik

c = rozwiaz_uklad_trojdiagonalny([wiersz[:] for wiersz in A], b[:])

#krok 4 - wyznaczenie współczynników splinow na każdym przedziale
wspolczynniki_splajnow = []

for i in range(n - 1):
    a_i = y[i]
    b_i = (y[i + 1] - y[i]) / h[i] - h[i] * (2 * c[i] + c[i + 1]) / 3
    c_i = c[i]
    d_i = (c[i + 1] - c[i]) / (3 * h[i])

    wspolczynniki_splajnow.append((a_i, b_i, c_i, d_i))

print("Współczynniki:")
print("Postać lokalna: S_i(x) = a_i + b_i*(x - x_i) + c_i*(x - x_i)^2 + d_i*(x - x_i)^3")
print()

for i in range(n - 1):
    a_i, b_i, c_i, d_i = wspolczynniki_splajnow[i]
    print(f"Przedział [{x[i]}, {x[i + 1]}]:")
    print(f"a_{i} = {a_i:.6f}")
    print(f"b_{i} = {b_i:.6f}")
    print(f"c_{i} = {c_i:.6f}")
    print(f"d_{i} = {d_i:.6f}")
    print("-" * 30)

print("Współczynniki c_i w węzłach:")
for i in range(n):
    print(f"c_{i} = {c[i]:.6f}")