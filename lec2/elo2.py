numb: list = [
    1, 2, 3,4, 5, 6, 7, 8, 9
]

for n in numb:
    if n % 3 == 0:
        print(f'Число - {n} tree')
    elif n % 5 == 0:
        print(f'Число - {n} pyat')
    else:
        print(f'Число - {n} nitonito')