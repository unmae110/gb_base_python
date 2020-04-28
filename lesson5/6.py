with open("school", "r") as f:
    lessons = {}
    for line in f:
        tmp=line.split()
        name = tmp[0].split(':')[0]
        lessons[name] = tmp[1:]
result={}
for key, value in lessons.items():
    result[key] = sum([int(itm.split('(')[0]) for itm in value if \
                       itm.split('(')[0].isdigit()])
print(result)