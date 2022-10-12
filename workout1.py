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

print('************************')
def gen(x):
    yield from range(x)

print(gen(5))

print('************************')

class Foo:
    x = 1
    def __init__(self):
        self.y = 2

foo = Foo()
foo.z = 3

print(len(foo.__dict__))


print([1, 2, 3] == {1, 2, 3})
print([1, 2, 3] == (1, 2, 3))