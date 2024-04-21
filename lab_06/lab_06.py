import csv
import datetime
from random import random, randint


# Zadanie 1
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

with open('zamowienia_polska.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(kolumny)
    for wiersz in poland:
        writer.writerow(wiersz)

with open('zamowienia_niemcy.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(kolumny)
    for wiersz in germany:
        writer.writerow(wiersz)


# Zadanie 2
def scal(files: list, newfile: str) -> None:
    with open(newfile, 'w', newline='') as f:
        for file in files:
            with open(file, 'r', newline='') as fi:
                for row in fi:
                    f.write(row)


scal(['zamowienia_polska.csv', 'zamowienia_niemcy.csv'], 'new.csv')


# Zadanie 3
def n_min_max(numbers: list[float | int], n: int, min_max: bool = False) -> list:
    if all(isinstance(x, (int, float)) for x in numbers):
        sort_num = numbers.copy()
        sort_num.sort(reverse=min_max)
        return sort_num[:n]
    else:
        return ["Lista nie zawiera tylko liczb"]


num = [5, 7, 9, 3, 0.9, 17]
nie = ['slowo', 'f', 0, 8]
print(n_min_max(num, 3, True))
print(n_min_max(num, 3))
print(n_min_max(nie, 2))


# Zadanie 4
mieszana = [1, 2.3, 'Sara', 5, 'Marian', 3.0]
slownik = dict()
for x in mieszana:
    if type(x).__name__ not in slownik.keys():
        slownik[type(x).__name__] = [x]
    else:
        slownik[type(x).__name__].append(x)
print(slownik)


# Zadanie 5
def podziel(nazw: list[str]):
    with open('A-M_nazwiska.txt', 'w', encoding='utf-8', newline='') as am:
        with open('N-Ż_nazwiska.txt', 'w', encoding='utf-8', newline='') as nz:
            for nazwisko in nazw:
                if ord(nazwisko[0].upper()) <= 77:
                    am.write(nazwisko+'\n')
                else:
                    nz.write(nazwisko+'\n')


nazwiska = ['Górski', 'Wysocki', 'Pietruszka', 'Kowalski', 'Źdźbło']
podziel(nazwiska)


# Zadanie 6
def odwrot(txt: str) -> str:
    new_txt = ""
    for slowo in txt.split(' '):
        new_txt += slowo[::-1]+" "
    return new_txt


print(odwrot("Ala ma kota"))


# Zadanie 7
def gra_karty() -> list():
    kolory = ['pik', 'karo', 'trefl', 'czerwo']
    figury = ['as', 'król', 'dama', 'walet'] + [str(x) for x in range(10, 1, -1)]
    karty = [fig + ' ' + kol for kol in kolory for fig in figury]
    gracze = []
    for i in range(4):
        reka = []
        for j in range(5):
            karta = karty[randint(0, len(karty)-1)]
            reka.append(karta)
            karty.remove(karta)
        gracze.append(reka)
    return f'Artur: {gracze[0]}\nAdam: {gracze[1]}\nMarcel: {gracze[2]}\nMarta: {gracze[3]}\n'


print(gra_karty())


# Zadanie 8
def adresy(plik: str, domena: str) -> None:
    pl = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    with open('osoby.txt', 'r', encoding='utf-8') as wejscie:
        with open(plik, 'w', encoding='utf-8') as wyjscie:
            for wiersz in wejscie:
                osoba = wiersz.strip()
                adres = osoba.lower().replace(' ', '.')
                for znak, zmiana in pl.items():
                    adres = adres.replace(znak, zmiana)
                wyjscie.write(adres+f'@{domena}\n')


adresy('adresy.txt', 'student.uwm.edu.pl')


# Zadanie 9
def losuj_haslo():
    with open('hasla.txt', 'r', encoding='utf-8') as f:
        return random.choice(f.readlines()).strip()


def wyswietl_haslo(haslo, zgadniete_litery):
    return " ".join(litera if litera.lower() in zgadniete_litery.lower() or litera == " " else "_" for litera in haslo)


def gra():
    haslo = losuj_haslo()
    zgadniete_litery = ""

    print("Koło fortuny")
    print("Hasło do odgadnięcia:")
    print(wyswietl_haslo(haslo, zgadniete_litery))

    while True:
        ruch = input("Podaj 1 literę lub wpisz całe hasło: ")

        if len(ruch) == 1 and ruch.isalpha():
            if ruch.lower() in zgadniete_litery.lower():
                print("Ta litera została już podana")
            elif ruch.lower() in haslo.lower():
                zgadniete_litery += ruch
                print("Brawo! Litera '{}' znajduje się w haśle".format(ruch))
            else:
                print("Litera '{}' nie występuje w haśle".format(ruch))
        elif len(ruch) > 1:
            if ruch.lower() == haslo.lower():
                print("Gratulacje! Hasło prawidłowe")
                break
            else:
                print("Błędne hasło")
        else:
            print("Niepoprawne dane. Podaj literę lub całe hasło")

        print(wyswietl_haslo(haslo, zgadniete_litery))

        if "_" not in wyswietl_haslo(haslo, zgadniete_litery):
            print("Gratulacje! Odgadłeś hasło")
            break


gra()
