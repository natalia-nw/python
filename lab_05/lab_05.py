import math
from random import random, randint

# Zadanie 1
A = [1 / x for x in range(1, 11)]
B = [pow(2, x) for x in range(11)]
C = [x for x in B if x % 4 == 0]
print(A, B, C, sep='\n')


# Zadanie 2
macierz = [[random() for y in range(4)] for x in range(4)]
przekatna = [macierz[i][i] for i in range(4)]
print(macierz, przekatna, sep='\n')


# Zadanie 3
text = 'Ala ma kota.'
generator = ((x, [ord(y) for y in x]) for x in text.split(" "))
for x in generator:
    print(x)


# Zadanie 4
def row_kwadratowe(a: int, b: int, c: int) -> float:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        # brak pierwiastków
        return -1
    elif delta == 0:
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2


print(row_kwadratowe(6, 1, 3))
print(row_kwadratowe(1, 2, 1))
print(row_kwadratowe(1, 4, 1))


# Zadanie 5
def rzut_k6(n: int) -> list():
    kostka = dict.fromkeys([x for x in range(1, 7)], 0)
    for x in range(n):
        rzut = randint(1, 6)
        kostka[rzut] += 1
    return [(f'oczka: {x}', f'rzutów: {kostka[x]}') for x in range(6, 0, -1)]


n = int(input("Podaj ilość rzutów: "))
print(rzut_k6(n))


# Zadanie 6
def abc(*txt: str) -> list():
    if len(txt) == 0:
        return list()
    else:
        return sorted([x for x in txt])


print(abc('auto', 'chleb', 'a', 'kot', 'abc'))


# Zadanie 7
def pkt(** nazwa: dict()) -> int:
    return sum([nazwa[x] for x in nazwa])


print(pkt(team1=5, team2=3, team3=7))
