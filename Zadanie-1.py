mounth = int(input("Введите число от от 1 до 12: "))
if 1 <= mounth <= 2 or mounth == 12:
    print("Зима")
if 3 <= mounth <= 5:
    print("Весна")
if 6 <= mounth <= 8:
    print("Лето")
if 9 <= mounth <= 11:
    print("Осень")
if mounth <= 0 or mounth > 12:
    print("В году только 12 месяцев! Попробуйте еще раз.")

