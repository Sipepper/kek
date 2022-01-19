print('Введите 2-х, 3-х или 4-х значное число')
# Строки в работе алгоритма не будут использованы
number = int(input())
# Преобразование строки, введённой пользователем, в натуральное число
if number - 99 < 0:
    ones = number % 10
    tenth = number // 10
    final = 10 * ones + tenth
    print(final)
# Так как проверка условий идёт по строчно нам не неужно при проверке числа на 2-х 3-х и т.д. значность
# указывать дополнительное условие т.е. (number - 999 < 0) and (number - 99 > 0)
elif number - 999 < 0:
    ones = number % 100 % 10
    tenth = number // 10 % 10
    hundreds = number // 100
    final = 100 * ones + 10 * tenth + hundreds
    print(final)
elif number - 9999 < 0:
    ones = number % 10
    tenth = number % 100 // 10
    hundreds = number % 1000 // 100
    thousands = number // 1000
    final = 1000 * ones + 100 * tenth + 10 * hundreds + thousands
    print(final)
else:
    print('ваше число не подходит')
