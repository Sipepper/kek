height = int(input('Введите высоту фигуры '))
indexes = [*range(height)]+[*reversed(range(height-1))]
for _ in indexes:
    if indexes[_] == 0:
        print('kek')
print(indexes)
# for _ in indexes:
#     if indexes.index(_) <= height:
