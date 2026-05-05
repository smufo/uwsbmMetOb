def zamien_wiersze(A, wiersz1, wiersz2):
    A[wiersz1], A[wiersz2] = A[wiersz2], A[wiersz1]
    print("Macierz po zamianie wierszy:")
    for wiersz in A:
        print(*wiersz)

def mnozenie_wiersza_przez_liczbe(A, wiersz, mnoznik):
    A[wiersz] = [x * mnoznik for x in A[wiersz]]
    print("Macierz po przemnożeniu wiersza przez liczbę:")
    for wiersz in A:
        print(*wiersz)

def dodanie_do_wiersza_wielokrotnosci_wiersza(A, wiersz1, wiersz2, mnoznik):
    A[wiersz1] = [a + b * mnoznik for a, b in zip(A[wiersz1], A[wiersz2])]
    print("Macierz po dodaniu do wiersza wielokrotności innego wiersza:")
    for wiersz in A:
        print(*wiersz)

#zamien_wiersze(A, 0, 1)
#mnozenie_wiersza_przez_liczbe(A, 0, 2)
#dodanie_do_wiersza_wielokrotnosci_wiersza(A, 0, 1, 2)

A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
B = [[8], [-1], [-3]]

def eliminacja_gaussa(A, B):
    for i in range(len(A)):
        A[i].append(B[i][0])

    n = len(A)

    for i in range(n):
        max_val = abs(A[i][i])
        max_val_row_index = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > max_val:
                max_val = abs(A[k][i])
                max_val_row_index = k

        A[i], A[max_val_row_index] = A[max_val_row_index], A[i]

        for k in range(i + 1, n):
            if A[i][i] == 0:
                continue
            mnoznik = A[k][i] / A[i][i]
            for j in range(i, n + 1):
                A[k][j] -= mnoznik * A[i][j]

    print("Macierz po eliminacji:")
    for wiersz in A:
        print(*wiersz)

eliminacja_gaussa(A, B)