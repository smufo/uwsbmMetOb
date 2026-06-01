A = [[2, 1, -1], [-3, -1, 2],[-2, 1, 2]]
B = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

def zwroc_wymiary(M):
    wiersze = len(M)
    kolumny = len(M[0])
    return wiersze, kolumny

def wypisz_macierz(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=" ")
        print()

def dodaj_macierze(A, B):
    if zwroc_wymiary(A) != zwroc_wymiary(B):
        print("Nie można dodać macierzy o różnych wymiarach")
        return None
    wynikowa = [[0] * len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            wynikowa[i][j] = A[i][j] + B[i][j]

    wypisz_macierz(wynikowa)
    return wynikowa

def odejmij_macierze(A, B):
    if zwroc_wymiary(A) != zwroc_wymiary(B):
        print("Nie można odejmować macierzy o różnych wymiarach")
        return None
    wynikowa = [[0] * len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            wynikowa[i][j] = A[i][j] - B[i][j]

    wypisz_macierz(wynikowa)
    return wynikowa

def przemnoz_macierz(A, mnoznik):
    wynikowa = [[0]*len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            wynikowa[i][j] = A[i][j] * mnoznik

    wypisz_macierz(wynikowa)
    return wynikowa

def transponuj_macierz(M):
    wynikowa = [[0] * len(M) for i in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            wynikowa[j][i] = M[i][j]

    wypisz_macierz(wynikowa)
    return wynikowa

def mnozenie_macierzy(A, B):
    if (zwroc_wymiary(A))[1] != (zwroc_wymiary(B))[0]:
        print("Nie można mnożyć macierzy o niezgodnych wymiarach")
        return None

    wynikowa = [[0]*len(B[0]) for x in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                wynikowa[i][j] += A[i][k] * B[k][j]

    wypisz_macierz(wynikowa)
    return wynikowa

dodaj_macierze(A, B)
print('------')
odejmij_macierze(A, B)
print('------')
przemnoz_macierz(A, 2)
print('------')
transponuj_macierz(A)
print('------')
mnozenie_macierzy(A, B)