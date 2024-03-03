# Zadanie 1
txt1 = input('Wpisz dowolne zdanie: \n')
sep_zr = input('Wpisz separator źrodłowy: \n')
sep_cel = input('Wpisz separator docelowy: \n')

split_txt1 = txt1.split(sep_zr)
txt1 = sep_cel.join(split_txt1)

print(f'Zdanie po zmianie: \n {txt1} \n')


# Zadanie 2
txt2 = input('Wpisz łańcuch znaków: \n')
dl = len(txt2)
polowa = int(dl / 2)

print(f'{txt2[:polowa:]}, {txt2[polowa::]}')
print(f'{txt2[::2]}')


# Zadanie 3
txt3 = 'losowy ciąg Znaków'

print(txt3.title())
print(txt3.capitalize())
print(txt3.zfill(25))
print(txt3.upper())
print(txt3.count('w'))
print(txt3.center(40))


# Zadanie 4
txt4 = input('Wpisz łańcuch znaków: \n')

print(f'Łańcuch {txt4} isalpha: {txt4.isalpha()}')
print(f'Łańcuch {txt4} isascii: {txt4.isascii()}')
print(f'Łańcuch {txt4} isprintable: {txt4.isprintable()}')
print(f'Łańcuch {txt4} istitle: {txt4.istitle()}')
print(f'Łańcuch {txt4} isupper: {txt4.isupper()}')
print(f'Łańcuch {txt4} isdecimal: {txt4.isdecimal()}')


# Zadanie 5
# print('{:>15}'.format('qwerty'))
# print('{:^10}'.format('qwerty'))
# print('{:.3}'.format('qwerty'))
# print('{:04d}'.format(23))
# print('{:=5d}'.format((- 37)))

txt5 = 'qwerty'
liczba1 = 23
liczba2 = -  37
print(f'{txt5:>15}')
print(f'{txt5:^10}')
print(f'{txt5:.3}')
print(f'{liczba1:04d}')
print(f'{liczba2:=5d}')


# Zadanie 6
print('\u00B6 U+00B6')
print('\u03BB U+03BB')
print('\u20AC U+20AC')
print('\u2140 U+2140')
print('\u222C U+222C')
print('\u2328 U+2328')
print('\u23FB U+23FB')
print('\u2728 U+2728')
print('\U0001F33C U+1F33C')
print('\U0001F43E U+1F43E')
