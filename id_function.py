a = 37
print(id(a))

a = a + 10
print(id(a))

x = 17 # x holds a pointer to the object 17
y = 17 # so does y

print(x is y)
print(id(x)) # the unique id associated with 17
print(id(y))

s1 = "abc" # creates a new string
s2 = "ab" + "c" # creates a new string

print(s1 is s2) # actually it doesn't
print(id(s1))
print(id(s2))

s3 = s2.upper() # uppercase s2
print(s3)
print(id(s3)) # this is a new string
