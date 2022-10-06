weight = input("Введите цифру и единицу измерения (вес, температура, длина): ")

if "t" in weight:
    q = (weight[:-1])
    print(f'{float(q) * 1000}kg')
    print(f'{float(q) * 1000000}g')
elif "kg" in weight:
    q = (weight[:-2])
    print(f'{float(q) / 1000}t')
    print(f'{float(q) * 1000}g')
elif "du" in weight:
    q = (weight[:-2])
    print(f'{float(q) * 2.54}cm')
elif "fr" in weight:
    q = (weight[:-2])
    print(f'{round(float(q) - 32) / 1.8}C°')
elif "c" in weight:
    q = (weight[:-1])
    print(f'{(float(q) * 1.8) + 32}Fr°')
else:
    q = (weight[:-1])
    print(f'{float(q) / 1000000}t')
    print(f'{float(q) / 1000}kg')
