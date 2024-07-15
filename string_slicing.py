s = 'The beatles'
t = s[4:8]
print(t)

u = s[4:] # same as s[4:11] Handy notation for ending slicing
print(u)

v = s[:4] # same as s[0:4] Handy notation for beginning slicing
print(v)

x = s[8:20] # it's OK to go beyond the end of the source string
print(x)

w = s[11] # Illegal to access