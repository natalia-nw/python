import sys

# Zadanie 1
for x in range(0, 51, 5):
    print(x)


# Zadanie 2
poziom = int(input("Wpisz wybraną wysokość 3, 5, 7 lub 9: "))
[print(f'{"o" * p:^{poziom}}') for p in range(1, poziom + 1, 2) if poziom in [3, 5, 7, 9]]
[print(f'{"o" * p:^{poziom}}') for p in range(poziom - 2, 0, -2) if poziom in [3, 5, 7, 9]]


# Zadanie 3
header = ''.join([f'{i:>5}' for i in [''] + list(range(1, 11))])
sep = f"\n{'':>3}{'-' * 53}"
rows = [f"\n{i:>4}|" + ''.join([f'{i * j:>5}' for j in range(1, 11)]) for i in range(1, 11)]
print(header + sep + ''.join(rows))


# Zadanie 4
liczba1 = input("Wpisz liczbę calkowitą: ")
print(f'Liczba {liczba1} w postaci binarnej: {bin(int(liczba1))}, '
      f'w postaci ósemkowej: {oct(int(liczba1))} oraz szesnastkowej: {hex(int(liczba1))}')


# Zadaanie 5
value = input("Podaj wartość: ")

try:
    int_value = int(value)
    print(f"'{value}' może być rzutowane na typ int.")
except ValueError:
    print(f"'{value}' nie może być rzutowane na typ int.")

try:
    float_value = float(value)
    print(f"'{value}' może być rzutowane na typ float.")
except ValueError:
    print(f"'{value}' nie może być rzutowane na typ float.")


# Zadanie 6
sys.stdout.write(f'Podaj liczbę całkowitą: ')
liczba = int(sys.stdin.readline())
liczba = str(liczba)
dl = len(liczba)
wynik = [f'{10 ** (dl - i - 1)} * {int(liczba[i])}' for i in range(dl)]
wynik = " + ".join(wynik)
sys.stdout.write(f'Podaną liczbę można zapisać jako: {wynik}')


# Zadaanie 7
print('\n')
import this

txt = input("\nWpisz tekst: ")
txt2 = ""
for x in txt:
    try:
        txt2 += this.d[x]
    except:
        txt2 += x
print(txt2)


# Zadanie 8
txt = input("Wpisz zdanie: ")
split_txt = txt.split(" ")
print(sorted(split_txt, key=len))


# Zadanie 9
import random

k1 = ['Koleżanki i koledzy ', 'Z drugiej strony ', 'Podobnie ', 'Nie zapominajmy jednak, że ', 'W ten oto sposób ',
      'Praktyka dnia codziennego dowodzi, że ',
      'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ ', 'Różnorakie i bogate doświadczenia ',
      'Troska organizacji, a szczególnie ', 'Wyższe założenia ideowe, a także ']
k2 = ['realizacja nakreślonych zadań programowych ', 'zakres i miejsce szkolenia kadr ',
      'stały wzrost ilości i zakres naszej aktywności ', 'aktualna struktura organizacji ',
      'nowy model działalności organizacyjnej ', 'dalszy rozwój różnych form działalności ',
      'stałe zabezpieczenie informacyjno programowe naszej działalności ', 'wzmacnianie i rozwijanie struktur ',
      'konsultacja z szerokim aktywem ', 'rozpoczęcie powszechnej akcji kształtowania postaw ']
k3 = ['zmusza nas do przeanalizowania ', 'spełnia istotną rolę w kształtowaniu ', 'wymaga sprecyzowania i określenia ',
      'pomaga w przygotowaniu i realizacji ', 'zabezpiecza udział szerokiej grupie w kształtowaniu ',
      'spełnia ważne zadania w wypracowaniu ', 'umożliwia w większym stopniu tworzenie ', 'powoduje docenianie wagi ',
      'przedstawia intersującą próbę sprawdzenia ', 'pociąga za sobą proces wdrażania i unowocześniania ']
k4 = ['istniejących warunków administracyjno- finansowych. ', 'dalszych kierunków rozwoju. ',
      'systemu powszechnego uczestnictwa. ', 'postaw uczestników wobec zadań stawianych przez organizację. ',
      'nowych propozycji. ', 'kierunków postępowego wychowania. ',
      'systemu szkolenia kadry odpowiadającego potrzebom. ', 'odpowiednich waruknków aktywizacji. ', 'modelu rozwoju. ',
      'form oddziaływania. ']


def generuj():
    zdanie = [random.choice(k1), random.choice(k2), random.choice(k3), random.choice(k4)]
    return ' '.join(zdanie)


n = int(input("Podaj ilość zdań: "))
for x in range(n):
    print(generuj())
