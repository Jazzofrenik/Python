all_students = int(input('Введите количество учеников: '))
student = 0
all_3 = 0
all_4 = 0
all_5 = 0
for student in range(all_students):
    student += 1
    # print('Оценка ', student, '-го студента - ')
    mark = int(input('Оценка ' + str(student) + '-го ученика: '))
    if mark == 3:
        all_3 += 1
    elif mark == 4:
        all_4 += 1
    elif mark == 5:
        all_5 += 1
print('Всего отличников: ', all_5)
print('Всего хорошистов: ', all_4)
print('Всего троечников: ', all_3)
if all_4 < all_3 > all_5:
    print('Больше всего троечников')
elif all_3 < all_4 > all_5:
    print('Больше всего хорошистов')
else:
    print('Больше всего отличников')
