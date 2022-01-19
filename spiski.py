import random
len1 = int(input('Input first list length'))
len2 = int(input('Input second list length'))

# list_1 = sorted([random.randint(0,200) for _ in range(len1)])
# list_2 = sorted([random.randint(0,200) for _ in range(len2)])

list_1 = [1,2,3,5]
list_2 = [1,2,4,5]
print(list_1)
print(list_2)

uniq = []
for i in list_1:
    for j in list_2:
        if i == j:
            list_1.remove(i)
            list_2.remove(i)
print(list_1+list_2)

uniqa = [x for x in list_1 for y in list_2 if x == y]
print(uniqa)