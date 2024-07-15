numbers = [2,3,11,7]
for i in numbers:
    print('Current number is',i)
    if i > 10:
        continue
    square = i*i
    print('Square of a current number is',square)