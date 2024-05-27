import csv
import datetime
from typing import Any, Callable


# Zadanie 1
def extract_numbers(vals: list[Any]) -> list[int | float]:
    return list(filter(lambda x: isinstance(x, (int, float)), vals))


print(extract_numbers(["slowo", 5, 7.3, -1, "tekst", -4.4]))


# Zadanie 2
wyrazy = input('Lista wyrazów: ')
print(sorted(wyrazy.split(), key=lambda x: len(x), reverse=True))


# Zadanie 3
def int_str_sort(elem: list[int | str], reversed: bool = False) -> list[int | str]:
    return sorted(filter(lambda x: isinstance(x, str), elem)) + sorted(filter(lambda x: isinstance(x, int), elem)) \
        if reversed else sorted(filter(lambda x: isinstance(x, int), elem)) + \
                         sorted(filter(lambda x: isinstance(x, str), elem))


print(int_str_sort(["slowo", 1, -3, 5, "wyrazy"], True))
print(int_str_sort(["slowo", 1, -3, 5, "wyrazy"], False))
print(int_str_sort(["slowa", 'a', 'abc', "wyrazy"], True))
print(int_str_sort([1, 4, -5, 0, 7], False))


# Zadanie 4
poland = []
germany = []
kolumny = []

with open('zamowienia.csv', newline='', encoding="utf8", errors="ignore") as plik:
    reader = csv.reader(plik, delimiter=';', quoting=csv.QUOTE_NONE)
    kolumny = next(reader, None)
    for wiersz in reader:
        wiersz[4] = wiersz[4][:-2].replace(",", ".").replace(" ", "")
        date = wiersz[2].split(".")
        wiersz[2] = datetime.datetime(int(date[2]), int(date[1]), int(date[0])).strftime("%Y-%m-%d")
        if wiersz[0] == "Polska":
            poland.append(wiersz)
        else:
            germany.append(wiersz)

with open('zamowienia_polska2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(kolumny)
    for wiersz in poland:
        writer.writerow(wiersz)

with open('zamowienia_niemcy2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(kolumny)
    for wiersz in germany:
        writer.writerow(wiersz)


# Zadanie 5
def sort_dict(dictionary: dict, arg: Callable) -> dict:
    return dict(sorted(dictionary.items(), key=lambda x: arg(list(x)[1:][0])))


slownik = {'Jan': [11, 13, 8, 7], 'Andrzej': [5, 14, 1, 0], 'Stanisław': [12, 9, 6, 14]}
print(sort_dict(slownik, min))
print(sort_dict(slownik, max))
print(sort_dict(slownik, sum))

