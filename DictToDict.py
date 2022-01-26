import string as s
import random as r

# a = random.sample(range(0, len(string.ascii_letters)-10), len(string.ascii_letters)-1)

dict_1 = {s.ascii_letters[r.randint(0,i)]: r.randint(0,42) for i in range(0,len(s.ascii_letters)//2)}
dict_2 = {s.ascii_letters[r.randint(0,i)]: r.randint(0,42) for i in reversed(range(0,len(s.ascii_letters)//2))}

a = list(dict_2.keys())+list(dict_1.keys())

emp_dict = {}
for i in set(a):
    if i not in dict_1.keys():
        emp_dict = emp_dict.update({i: dict_2.get(i)})
    elif i not in dict_2.keys():
        emp_dict = emp_dict.update({i: dict_1.get(i)})



print(dict_1,'\n',dict_2,'\n',emp_dict, )
