seasons = ['autumn', 'winter', 'spring', 'summer']
x = int(input('Type number of month: '))

if x <= 2 or x == 12:
    print(seasons[1])
if 3 <= x <= 5:
    print(seasons[2])
if 6 <= x <= 8:
    print(seasons[3])
if 9 <= x <= 11:
    print(seasons[0])
