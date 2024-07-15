a,b,c = 1,2,3 # Simultaneous assignment
print(a,b,c)

# Swap using third variable or temp variable 
x = 10 
y = 20
temp = x
x = y
y = temp
print(x, y)

# Swap without using third variable
a = 20
b = 30
a,b = b,a
print(a,b)
