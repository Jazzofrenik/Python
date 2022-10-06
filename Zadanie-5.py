text = input("Введите текст с разной высотой букв: ")

print(f'{sum(map(str.isupper, text))}')
print("")
print("------------------------------------------------")
print("")
text = input("Введите текст с разной высотой букв: ")
upper = 0
i = 0
while i < len(text):
    if text[i].isupper():
        upper += 1
    i += 1
print(upper)
