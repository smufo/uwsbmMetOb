A = [[2, 1, -1, 8], [-3, -1, 2, -1],[-2, 1, 2, -3]]

def zwroc_wymiary(M):
    wiersze = len(M)
    kolumny = len(M[0])
    return wiersze, kolumny

def dodaj_macierze(A, B):
    if zwroc_wymiary(A) != zwroc_wymiary(B):
        print("Nie można dodać macierzy o różnych wymiarach")
        return None
    wynikowa = [[0] * len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            wynikowa[i][j] = A[i][j] + B[i][j]

    print("Wynik dodawania to macierz:")
    for i in range(len(wynikowa)):
        for j in range(len(wynikowa[0])):
            print(wynikowa[i][j], end=" ")
        print()
    return wynikowa

def odejmij_macierze(A, B):
    if zwroc_wymiary(A) != zwroc_wymiary(B):
        print("Nie można odejmować macierzy o różnych wymiarach")
        return None
    wynikowa = [[0] * len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            wynikowa[i][j] = A[i][j] - B[i][j]

    print("Wynik odejmowania to macierz:")
    for i in range(len(wynikowa)):
        for j in range(len(wynikowa[0])):
            print(wynikowa[i][j], end=" ")
        print()
    return wynikowa

def przemnoz_macierz(A):
    mnoznik = int(input("Podaj mnożnik: "))
    wynikowa = [[0]*len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            wynikowa[i][j] = A[i][j] * mnoznik

    print("Wynik przemnożenia macierzy przez liczbę:")
    for i in range(len(wynikowa)):
        for j in range(len(wynikowa[0])):
            print(wynikowa[i][j], end=" ")
        print()
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

    print("Wynik mnożenia macierzy przez macierz:")
    for i in range(len(wynikowa)):
        for j in range(len(wynikowa[0])):
            print(wynikowa[i][j], end=" ")
        print()
    return wynikowa
