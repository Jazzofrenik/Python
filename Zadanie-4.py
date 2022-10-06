def new():

    list1 = input("Введите любые числа через пробел: ").strip().split()

    def multiply_list(my_list):
        result = 1
        for n in my_list:
            result = result * int(n)
        return result


    print(multiply_list(list1))

    digit = input("Type any digit: ")

    def plusone():
        n = int(digit) + 1
        return n


    print(plusone())

new()