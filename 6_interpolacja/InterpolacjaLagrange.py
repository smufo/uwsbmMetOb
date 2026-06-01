wezly_xy = [[1.0, 2.0, 4.0, 5.0, 7.0],[2.0, 4.5, 1.5, 5.0, 3.0]]
wspolczynniki_A = []

def mnozenie_wielomianow(w1, w2):
    wynik = [0] * (len(w1) + len(w2) - 1)
    for i_w1 in range(len(w1)):
        for i_w2 in range(len(w2)):
            wynik[i_w1 + i_w2] += w1[i_w1] * w2[i_w2]
    return wynik

for i in range(len(wezly_xy[0])):
    wspolczynniki_A.append(0)

for i in range(len(wezly_xy[0])):
    mianownik = 1
    licznik = [1]
    for j in range(len(wezly_xy[0])):
        if i != j:
            mianownik *= (wezly_xy[0][i] - wezly_xy[0][j])
            czynnik = [1, -wezly_xy[0][j]]
            licznik = mnozenie_wielomianow(licznik, czynnik)

    skala = wezly_xy[1][i] / mianownik
    for k in range(len(licznik)):
        wspolczynniki_A[k] += licznik[k] * skala

print("Współczynniki wielomianu interpolacyjnego Lagrange'a:", wspolczynniki_A)