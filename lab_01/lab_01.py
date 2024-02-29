# Zadanie 1
int1 = int(0b100101)
int2 = 17
float1 = float(-0b010111)
float2 = 7.5

print(f'Obiekty typu int: {int1}, {int2}')
print(f'Obiekty typu float: {float1}, {float2}')


# Zadanie 2
int_bit = [-1, 255]
float_int = [4.3, 9.0]

for x in int_bit:
    n = x.bit_count()
    print(f'W binarnej reprezentacji |{x}| 1 występuje {n} razy')

for x in float_int:
    if x.is_integer():
        print(f'{x} może być int')
    else:
        print(f'{x} nie jest int')


# Zadanie 3
liczba = 5
bin1 = bin(liczba)
int3 = int(bin1, 2)

print(f'Liczba {liczba} po konwersji na binarną: {bin1} i ponownie na całkowitą: {int3}')


# Zadanie 4
x = 0b10
y = 0b1011
ob1 = x & y
ob2 = x << 2
ob3 = ~y
ob4 = x ^ y
print(f'{x} & {y} = {ob1}')
print(f'{x} << 2 = {ob2}')
print(f'~{y} = {ob3}')
print(f'{x} ^ {y} = {ob1}')


# Zadanie 5
liczba2 = 5.7
hex1 = float.hex(liczba2)
float3 = float.fromhex(hex1)

print(f'Liczba {liczba2} po konwersji do postaci hex: {hex1} i ponownie do float: {float3}')
