height = int(input('Введите высоту фигуры: '))
for i in range(height):
    if i == 0:
        line = (height - i) * ' ' + '*' + (height - i) * ' '
        print(line)
    elif i < height - 1:
        line = (height - i) * ' ' + '*' + (2 * i - 1) * ' ' + '*' + (height - i) * ' '
        print(line)
    else:
        line = ' ' + (2 * height - 1) * '*'
        print(line)
j = 1
while j <= height:
    line = (height - j) * ' ' + (2 * j - 1) * '*' + (height - j) * ' '
    print(line)
    j += 1
k = 1
while k <= 2 * height - 1:
    if k <= height:
        line = (height - k) * ' ' + (2 * k - 1) * '*' + (height - k) * ' '
        print(line)
    elif (k > height) and (k < 2 * height - 1):
        line = (k - height) * ' ' + '*' + (4 * height - 2 * k - 3) * ' ' + '*' + (k - height) * ' '
        print(line)
    else:
        line = (k - height) * ' ' + '*' + (k - height) * ' '
        print(line)
    k += 1
k = 1
while k <= 2 * height - 1:
    if k <= height:
        line = (height - k) * ' ' + (2 * k - 1) * '*' + (height - k) * ' '
        print(line)
    elif (k > height) and (k < 2 * height - 1):
        odd_things = 2 * (height - 1) - k
        line = (k - height) * ' ' + '*' + odd_things * ' ' + '*' + odd_things * ' ' + '*' + (k - height) * ' '
        print(line)
    else:
        line = (k - height) * ' ' + '*' + (k - height) * ' '
        print(line)
    k += 1
