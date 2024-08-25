def increment_x(x):
    x += 1
    print('Value of x in the function increment_x =', x)

def reverse_list(lst):
    lst.reverse()
    print('list in the function reverse_list =', lst)

print()
x = 3
print('x before function call:', x)
increment_x(x)
print('x after function call: ',x)
print()

lst = [2,3,4,5,11]
print('list before function call:', lst)
reverse_list(lst)
print('list after function call', lst)