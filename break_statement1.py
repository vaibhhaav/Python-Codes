name = 'python programming'
size = len(name)
i = 0
while i < size:
    if name[i].isspace():
        break
    print(name[i],end='')
    i = i + 1