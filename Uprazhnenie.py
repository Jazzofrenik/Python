# while True:
#     a = int(input())
#     if a < 50:
#         continue
#     if a > 100:
#         break
#     print(a)
# print("Работа программы завершена")

# print("-----------")
#
# a = 1
# sum = 0
# while a !=0:
#     a = int(input())
#     sum += a
# print(sum)
#
# print("-----------")

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(c, d + 1):
    print("\t", '  ' + str(i), end = '')
print()
for i in range(a, b + 1):
    print(i, '', '\t', end='')
    for j in range(c, d + 1):
        print(i * j, ' ', end='\t')
        if j == d:
            print()

print("-----------")
# sum = int(input())
# n = int(input())
# for i in range(1, n + 1):
#     sum += sum * 0.07
# print(round(sum, 2))

numbers = list(range(1, 11))


print(alphabet)


