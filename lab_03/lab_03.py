# Zadanie 1
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista2 = lista1[5::]
lista1 = lista1[:5:]

print(lista1)
print(lista2)


# Zadanie 2
lista3 = lista1 + lista2
lista3.insert(0, 0)
lista4 = lista3.copy()
lista4.sort(reverse=True)

print(lista3)
print(lista4)


# Zadanie 3
txt1 = input('Wpisz tekst: \n').lower()
litery = [*txt1]
uni = []
for x in litery:
    if x not in uni:
        uni.append(x)
uni.sort()
print(uni)


# Zadanie 4
pl = {1: 'styczeń', 2: 'luty', 3: 'marzec', 4: 'kwiecień', 5: 'maj', 6: 'czerwiec',
      7: 'lipiec', 8: 'sierpień', 9: 'wrzesień', 10: 'październik', 11: 'listopad', 12: 'grudzień'}


# Zadanie 5
en = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july',
      8: 'august', 9: 'september', 10: 'october', 11: 'november', 12: 'december'}

months = dict()
months['pl'] = pl
months['en'] = en

print(months['pl'][4], months['en'][4])


# Zadanie 6
txt2 = 'Marianna'
slownik = dict.fromkeys(txt2, 1)

print(slownik)


# Zadanie 7
import string

txt3 = input('Wpisz tekst: \n').lower()

liter = set(txt3) & set(string.ascii_lowercase)
cyfr = set(txt3) & set(string.digits)

print(f'Tekst zawiera {len(txt3)} znaków')
print(f'Ilość znaków pokrywających się z string.ascii_lowercase: {len(liter)}, czyli: {(len(liter) / len(string.ascii_lowercase)) * 100:.2f}%')
print(f'Ilość znaków pokrywających się z string.digits: {len(cyfr)}, czyli: {(len(cyfr) / len(string.digits)) * 100:.2f}%')
