from timeit import timeit
import random
from array import array
import csv
from datetime import datetime
import time
from collections import deque, namedtuple, Counter
from typing import Any
import numpy as np


# Zadanie 1
setup = """
from array import array
import random
import string
"""
stmt1 = """
tab_of_chars = array('u', random.choices(string.ascii_letters, k=1_000_000))
"""
stmt2 = """
list_of_chars = random.choices(string.ascii_letters, k=1_000_000)
"""
stmt3 = """
tab_of_ints = array('i', (random.randint(0, 100) for _ in range(1_000_000)))
"""
stmt4 = """
list_of_ints = [random.randint(0, 100) for _ in range(1_000_000)]
"""
stmt5 = """
tab_of_longs = array('l', (random.randint(0, 100) for _ in range(1_000_000)))
"""
stmt6 = """
list_of_longs = [random.randint(0, 100) for _ in range(1_000_000)]
"""

print('tablica znaków:', timeit(stmt1, setup, number=10))
print('lista znaków:', timeit(stmt2, setup, number=10))
print('tablica int:', timeit(stmt3, setup, number=10))
print('lista int:', timeit(stmt4, setup, number=10))
print('tablica long:', timeit(stmt5, setup, number=10))
print('lista long:', timeit(stmt6, setup, number=10))


# Zadanie 2
tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])
list_of_floats = [random.random() for _ in range(1_000_000)]

start = datetime.now()
with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)
end = datetime.now()
print("zapis tablicy:", end - start)

start = datetime.now()
tab_of_floats_loaded = array('f')
with open('floats_array.bin', 'rb') as file_arr:
    tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
end = datetime.now()
print("ładowanie tablicy:", end - start)

start = datetime.now()
with open('floats_list.txt', 'w') as file_list:
    file_list.writelines('\n'.join([str(x) for x in list_of_floats]))
end = datetime.now()
print("zapis listy:", end - start)

start = datetime.now()
with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()
list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
end = datetime.now()
print("ładowanie listy:", end - start)


# Zadanie 3
setup = """
from collections import deque
kolejka = deque('Ala ma kota'.split())
"""
stmt1 = """
for x in range(100_000):
    kolejka.append('?')
"""
stmt2 = """
for x in range(100_000):
    kolejka.appendleft('Czy')
"""
print('deque append:', timeit(stmt1, setup, number=1))
print('deque append left:', timeit(stmt2, setup, number=1))

setup = """
lista = 'Ala ma kota'.split()
"""
stmt1 = """
for x in range(100_000):
    lista.append('?')
"""
stmt2 = """
for x in range(100_000):
    lista.insert(0,'Czy')
"""
print('list append:', timeit(stmt1, setup, number=1))
print('list insert:', timeit(stmt2, setup, number=1))


# Zadanie 5
liczby = sorted([random.randint(0, 100) for _ in range(30)])
print(liczby)
print(liczby[:(len(liczby)//10)])


# Zadanie 6
def create_kolo_fortuny(*args) -> deque:
    return deque(Counter(args).elements())


# Zadanie 7
def spinit(kolo: deque):

    kolo.rotate(random.randint(0, len(kolo)))

    print(f'Po obrocie: {kolo}')

    if kolo[0] != wygrana:
        time.sleep(1)
        spinit(kolo)


fortuna = create_kolo_fortuny('aaa', 'cvh', 'fdghf', 'qwerty')
print(f'Początkowy stan: {fortuna}')

wygrana = fortuna[0]
fortuna.rotate(1)
spinit(fortuna)
print('Wygrana')
