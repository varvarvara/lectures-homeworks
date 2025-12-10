a: list = []
b: tuple = () #unchangable
c1: set = {'how', 'are', 'you'} #to show empty set you need to use set() instead of {}
c2: set = {'are','you', 'fine'}
d1: dict = {'my_key': 'set 1', 'set': 'set 2'}
d2: dict = {'my_new_key': 'value_value', 'my key': 12}


#если полностью меня перемнную - то в тапл это невозможно, частично можно - надо исследовать этот вопрос  

#print(c)

# a[0] = 11
# a[-1] = 32
# print(a)

# x = 3
# y = x

# print(x is y, x == y, x, y)
# x += 3
# print(x is y, x == y, x, y)

# a.append(3)
# a.append(3)
# a.append(3)
# print(a.append(3))
# a.pop(3)
# print(a.pop(0))

# print(
#     a + [2, 3]
# )

# print(
#     a * [2, 3]
# )

#@ - скалярное произведение матриц  / a.T - транспонирование матриц
# np - многомерный 

print(c1 - c2)
print(c1.difference(c2))
print(c2.difference(c1))
print(c1.intersection(c2))
print(c2.intersection(c1))
print(c1)
c1.add('b') #there is no order in set
print(c1)

print(d1, d2)
