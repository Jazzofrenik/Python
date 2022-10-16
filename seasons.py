autumn = {'autumn': {'september': 9, 'october': 10, 'november': 11}}
winter = {'winter': {'december': 12, 'january': 1, 'february': 2}}
spring = {'spring': {'march': 3, 'april': 4, 'may': 5}}
summer = {'summer': {'june': 6, 'july': 7, 'august': 8}}

x = int(input('Type number of month: '))

if 1 <= x <= 2 or x == 12:
    print(winter)
elif 3 <= x <= 5:
    print(spring)
elif 6 <= x <= 8:
    print(summer)
elif 9 <= x <= 11:
    print(autumn)
else:
    print('Нет такого времени года.')
exit()
