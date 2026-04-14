def funkcja(x):
    return x**2 - 2

x0 = float(input('Podaj pierwszy punkt startowy x0: '))
x1 = float(input('Podaj drugi punkt startowy x1: '))
epsilon = float(input('Podaj tolerancję błędu: '))

while abs(funkcja(x1)) > epsilon:
    x0, x1 = x1, x1 - funkcja(x1) * (x1 - x0) / (funkcja(x1) - funkcja(x0))

print('Rozwiązaniem z dokładnością do', epsilon, 'jest x =', x1)