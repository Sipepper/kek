input_list = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
for i in input_list:
    name = i.get("name")
    parents = len(i.get("parents"))
    print('<'+name+'>'+':','<'+str(parents)+'>')
