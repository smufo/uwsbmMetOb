def funkcja(x):
    return x**2 - 2
def pochodna(x):
    return 2*x

xn = float(input('podaj punkt poczatkowy xn'))
epsilon = float(input('podaj tolerancje bledu'))

while abs(funkcja(xn)) > epsilon:
    xn = xn - funkcja(xn)/pochodna(xn)

print('Rozwiązaniem z dokładnością do', epsilon, 'jest xn = ', xn)