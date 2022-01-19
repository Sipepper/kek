import random

length = int(input('Input your list length'))
random_int_list = [random.randint(0,200) for x in range(length)]
print(random_int_list)
nlist = []
for i in random_int_list:
    if (i == random_int_list[0]) or (i == random_int_list[length-1]):
        continue
    elif (i > random_int_list[random_int_list.index(i)-1]) and (i > random_int_list[random_int_list.index(i)+1]):
        nlist.append(i)
    # else:
    #     continue
print(nlist)
print(len(nlist))