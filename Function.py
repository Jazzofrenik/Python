a = input("Salary: ")

def procent():
    x = (int(a) * 0.1494)     # Налог от нетто
    y = (int(a) + x)          # Сумма нетто
    z = (int(a) * 0.40)       # Аванс
    print("Налог от суммы нетто:", (f'{round(x)}'), "рублей.")
    print("Сумма нетто:", (f'{round(y)}'), "рублей.")
    print("Аванс:", (f'{round(z)}'), "рублей.")

procent()

print()
print("----------")
print("----------")
print()

def avans(w):
    money = w * 100 / 40
    print("Сумма:", (f'{round(money)}'), "рублей.")

avans(18640)