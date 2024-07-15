# Return the sum of values from 1 to n
def sum_to_n(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    return total

def main():
    print(sum_to_n(9))
    print(sum_to_n(1000))

main()

x = sum_to_n(30)
print(x)
print('Even' if sum_to_n(5)%2==0 else 'Odd')
for i in range(1,30):
    print(i, sum_to_n(i))