#Работа с циклом
# x = int(input("Введите число: "))
#
# while x <= 10:
#     print("Нужно число больше!")
#     x = int(input("Введите число: "))
# else:
#     print("Нормуль!")

print("------------")

#Работа со splitlines и split
text = "Доброе утро, страна!\nНастроение бодрое!"

x = text.splitlines()
print(x)

hello = "Hello, world! You are look great today!"

print(len(hello))
print(hello[1::37])

*r, = range(3)
print(r)

lst = [1, 2, 3]
print(lst.pop(1))

print()
print('---------------------------------')
print()
def gen(x):
    yield from range(x)
print(gen(5))

print()
print('---------------------------------')
print()
class Foo:
    x = 1
    def __init__(self):
        self.y = 2

foo = Foo()
foo.z = 3

print(len(foo.__dict__))


print([1, 2, 3] == {1, 2, 3})
print([1, 2, 3] == (1, 2, 3))

print('************************')
print('************************')

x = [0.1] * 10
print(sum(x))

print()
print('---------------------------------')
print()
class Foo:
    def __init__(self):
        self.__execute()

    def execute(self):
        print(1)

    __execute = execute

class Bar(Foo):
    def execute(self):
        print(2)

Bar()

print()
print('---------------------------------')
print()



print()
print('---------------------------------')
print()

x = list(range(10, 5))
print(x)

print()
print('---------------------------------')
print()

y = [[1]] * 4
print(y)
y[1][0] = 0

print(y[0][0])


# class Foo:
#     def __index__(self):
#         return '123'
#
# print(repr(int(Foo())))

print(int('16', 10))

