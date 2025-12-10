a: Ellipsis = ...
b: complex = complex(real=3,imag=-2) #imag = 2i
c: list = [b, a, 3, 4]
d: tuple = (b,2,3,4)
e: set = {'bob, ''hello', 'how', 'are', 'you'}
f: dict = {1: '11', 2: '22', 3: '33', 'bob': 'durak', 'new day': 'opyat durak'} 

print(
    f[1], f['bob']
)

print(f.keys()) #до :
print(f.values()) #после :

print(
    f['new day']['vova']
)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# print(
#     c[2], c[0], c[-1]
# )

# print(
#     c[1:4],
#     c[1:4],
#     c[0:46],
#     sep = '\n'
# )

# print('-'*10)
# print(
#     c[0:46:2] #start:stop:step
# )
# print(
#     c[::2]
# )

# print(
#     c[::-1]
# )
# переворачивает список

#print(d[::-1])

#print(e)

