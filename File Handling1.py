a = open(r"D:\B. Tech. VIT Bhopal\2nd Year (2024-2025)\3rd Semester (Fall Semester)\Python Programming\Python-codes\abc.txt",'w')

wl = []

for i in range(1,5):
    print("Please enter data: ")
    line = input()
    wl.append(line)

a.writelines(wl)

a.close()