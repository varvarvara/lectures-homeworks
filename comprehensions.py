a = []
for i in range(10):
    a.append(i**2)
print(a)

print([i**2 for i in range(10) if i % 2 == 0])
my_gen = (i**2 for i in range(10))

dict_comprehension = {str(v): v**2 for v in range(10) if v % 2 == 0}
print(dict_comprehension)
