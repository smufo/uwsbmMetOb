A = [[7, 2.5, 7.2], [2, 7, 3.3], [17, 0, 1]]
b = [3.7, 12, 3]

def zamien_wiersze(A, wiersz1, wiersz2):
    A[wiersz1], A[wiersz2] = A[wiersz2], A[wiersz1]
    print("Macierz po zamianie wierszy:")
    for wiersz in A:
        print(*wiersz)

def mnozenie_wiersza_przez_liczbe(A, wiersz, mnoznik):
    if mnoznik == 0:
        print("Nie można mnożyć wiersza przez zero")
        return None
    A[wiersz] = [x * mnoznik for x in A[wiersz]]
    print("Macierz po przemnożeniu wiersza przez liczbę:")
    for wiersz in A:
        print(*wiersz)

def dodanie_do_wiersza_wielokrotnosci_wiersza(A, wiersz1, wiersz2, mnoznik):
    A[wiersz1] = [a + b * mnoznik for a, b in zip(A[wiersz1], A[wiersz2])]
    print("Macierz po dodaniu do wiersza wielokrotności innego wiersza:")
    for wiersz in A:
        print(*wiersz)

def gauss_eliminacja(A, b):
    n = len(b)

    macierz_rozszerzona = [A[i][:] + [b[i]] for i in range(n)]
    print("Macierz rozszerzona ma postać:")
    for wiersz in macierz_rozszerzona:
        print(*wiersz)
    print()

    pivot = 0

    for col in range(n):
        if pivot >= n:
            break

        wiersz_pivota = None
        for r in range(pivot, n):
            if macierz_rozszerzona[r][col] != 0:
                wiersz_pivota = r
                break

        if wiersz_pivota is None:
            continue

        if wiersz_pivota != pivot:
            print(f"Zamiana wiersza {pivot} z wierszem {wiersz_pivota}:")
            zamien_wiersze(macierz_rozszerzona, pivot, wiersz_pivota)
            print()

        for r in range(pivot + 1, n):
            if macierz_rozszerzona[r][col] != 0:
                mnoznik = -macierz_rozszerzona[r][col] / macierz_rozszerzona[pivot][col]
                print(f"Zerowanie: wiersz {r} += {mnoznik:.4g} * wiersz {pivot}")
                dodanie_do_wiersza_wielokrotnosci_wiersza(macierz_rozszerzona, r, pivot, mnoznik)
                print()

        pivot += 1

    print("Postać schodkowa")
    for wiersz in macierz_rozszerzona:
        print(*[round(x, 6) for x in wiersz])
    print()

    ranga_A = 0
    ranga_M = 0
    for r in range(n):
        wspolczynniki = macierz_rozszerzona[r][:n]
        wyraz_wolny = macierz_rozszerzona[r][n]
        wiersz_zerowy = all(abs(x) < 1e-9 for x in wspolczynniki)

        if not wiersz_zerowy:
            ranga_A += 1
            ranga_M += 1
        elif abs(wyraz_wolny) > 1e-9:
            ranga_M += 1
            print(f"UWAGA: wiersz {r} to [0…0 | {round(wyraz_wolny, 6)}] → układ sprzeczny!")
            return "Układ sprzeczny – brak rozwiązań"

    if ranga_A < n:
        stopnie_swobody = n - ranga_A
        return (f"Układ nieoznaczony – nieskończenie wiele rozwiązań "
                f"(rg(A) = {ranga_A} < n = {n}, "
                f"{stopnie_swobody} parametr{'y' if 1 < stopnie_swobody < 5 else 'ów'} swobodnych)")

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        col_pivot = None
        for j in range(n):
            if abs(macierz_rozszerzona[i][j]) > 1e-9:
                col_pivot = j
                break
        if col_pivot is None:
            continue

        suma = sum(macierz_rozszerzona[i][j] * x[j] for j in range(col_pivot + 1, n))
        x[col_pivot] = (macierz_rozszerzona[i][n] - suma) / macierz_rozszerzona[i][col_pivot]

    print("Rozwiązanie metodą Gaussa")
    for i, xi in enumerate(x):
        print(f"x{i + 1} = {round(xi, 6)}")

    return [round(xi, 6) for xi in x]

gauss_eliminacja(A, b)

def gauss_jordan(A, b):
    n = len(b)
    macierz_rozszerzona = [A[i][:] + [b[i]] for i in range(n)]

    print("Macierz rozszerzona ma postać")
    for wiersz in macierz_rozszerzona:
        print(*wiersz)
    print()

    pivot = 0
    kolumny_pivot = []

    for col in range(n):
        if pivot >= n:
            break

        wiersz_pivota = None
        for r in range(pivot, n):
            if abs(macierz_rozszerzona[r][col]) > 1e-9:
                wiersz_pivota = r
                break

        if wiersz_pivota is None:
            continue

        if wiersz_pivota != pivot:
            print(f"Zamiana wiersza {pivot} z wierszem {wiersz_pivota}")
            zamien_wiersze(macierz_rozszerzona, pivot, wiersz_pivota)
            print()

        print(f"Normalizacja wiersza {pivot} (dzielenie przez {round(macierz_rozszerzona[pivot][col], 6)})")
        mnoznik_norm = 1.0 / macierz_rozszerzona[pivot][col]
        mnozenie_wiersza_przez_liczbe(macierz_rozszerzona, pivot, mnoznik_norm)
        print()

        for r in range(n):
            if r != pivot and abs(macierz_rozszerzona[r][col]) > 1e-9:
                mnoznik = -macierz_rozszerzona[r][col]
                print(f"Zerowanie elementu w wierszu {r}, kolumnie {col}")
                dodanie_do_wiersza_wielokrotnosci_wiersza(macierz_rozszerzona, r, pivot, mnoznik)
                print()

        kolumny_pivot.append(col)
        pivot += 1

    print("Postać schodkowa zredukowana:")
    for wiersz in macierz_rozszerzona:
        print(*[round(x, 6) for x in wiersz])
    print()

    for r in range(n):
        wspolczynniki = macierz_rozszerzona[r][:n]
        wyraz_wolny = macierz_rozszerzona[r][n]
        if all(abs(x) < 1e-9 for x in wspolczynniki):
            if abs(wyraz_wolny) > 1e-9:
                print(f"UWAGA: wiersz {r} to [0…0 | {round(wyraz_wolny, 6)}] → układ sprzeczny!")
                return "Układ sprzeczny – brak rozwiązań"

    wszystkie_kolumny = set(range(n))
    kolumny_swobodne = sorted(wszystkie_kolumny - set(kolumny_pivot))

    if kolumny_swobodne:
        stopnie = len(kolumny_swobodne)
        print(f"Zmienne bazowe:   x{[k + 1 for k in kolumny_pivot]}")
        print(f"Zmienne swobodne: x{[k + 1 for k in kolumny_swobodne]}")
        print()

        parametry = {col: f"t{i + 1}" for i, col in enumerate(kolumny_swobodne)}
        rozwiazanie = {}
        for col in kolumny_swobodne:
            rozwiazanie[col] = parametry[col]

        for i, col in enumerate(kolumny_pivot):
            wyraz = round(macierz_rozszerzona[i][n], 6)
            skladniki = []
            if abs(wyraz) > 1e-9:
                skladniki.append(str(wyraz))
            for col_sw in kolumny_swobodne:
                wsp = round(macierz_rozszerzona[i][col_sw], 6)
                if abs(wsp) > 1e-9:
                    skladniki.append(f"({-wsp})*{parametry[col_sw]}")
            rozwiazanie[col] = " + ".join(skladniki) if skladniki else "0"

        print("Rozwiązanie parametryczne")
        for i in range(n):
            print(f"x{i + 1} = {rozwiazanie.get(i, '?')}")

        return (f"Układ nieoznaczony – nieskończenie wiele rozwiązań "
                f"({stopnie} parametr{'y' if 1 < stopnie < 5 else 'ów'} swobodnych)")

    x = [0.0] * n
    for i, col in enumerate(kolumny_pivot):
        x[col] = macierz_rozszerzona[i][n]

    print("Rozwiązanie metodą Gaussa-Jordana")
    for i, xi in enumerate(x):
        print(f"x{i + 1} = {round(xi, 6)}")

    return [round(xi, 6) for xi in x]

gauss_jordan(A, b)