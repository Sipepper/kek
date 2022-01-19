import random

petya = int(input('Введите высоту Пети'))
number_of_students = int(input('Введите количество учеников в классе'))
heights_list = sorted([random.randint(100,200) for x in range(number_of_students)],reverse=True)
for _ in heights_list:
    if _ == petya:
        continue
    if _ < petya:
        heights_list = heights_list[0:heights_list.index(_)] + [petya] + heights_list[heights_list.index(_):]
        break
mesto = number_of_students - heights_list[::-1].index(petya) + 1
# print(heights_list)
print('Петя должен встать',mesto,'-ым номером')
