def inc_by_10(value:int): #и функция вернёт инт
    value += 1
    return value

# def no_return(value:int) -> int|None:
#     if value%2==0:
#         value*=10
#         if value == 20:
#             return
#         else: 
#             return value


# def print_to_console(init_value: int):
#     print(init_value)
#     init_value += 10
#     print('Hello')
#     print(init_value)

y = 1
    
def after_return() -> int:
    global y
    return inc_by_10(y)
    
def rec(x:int) -> int:
    print('recursion x =', x)
    if x < 100:
        x+=1
        x = rec(x)
    return x #отменил функцию рек - возвращение обратно через ретёрн

print(__name__)

if __name__ == 'f_in_f':
    print('I was imported')

if __name__ == '__main__':
    print(rec(0))
    print('hello from f_in_f')

# x = 1
# x = inc_by_10(x)

# print = (
#     inc_by_10(10)
# )

# print(no_return(2))
#print_to_console(2)