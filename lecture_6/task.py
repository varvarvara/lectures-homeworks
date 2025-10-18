# дополнить результат task2 предыдущей лекции (фибоначчи)
# самописным кэшем и проверить на больших числах
# для себя сравните скорости выполнения fib_cached и fib_regular
# на больших числах (больше 60)

n = int(input("Put an integer number: "))

# from functools import lru_cache

def fibonacci(n: int) -> int:
    # MY_CACHE: dict[int,int] = {}
    
    if n <=  0:
        return []
    
    elif n == 1:
        return [0]
    
    elif n == 2:
        return [0,1]
    
    s = [0,1]
    fib_1 = 0
    fib_2 = 1
    
    for i in range(2,n):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            s.append(fib_2)
            # MY_CACHE[n] = fib_2
            # print(f"{MY_CACHE} = ")
    return s

    
seq = fibonacci(n)
print(seq[-1])
