# дополнить результат task2 предыдущей лекции (фибоначчи)
# самописным кэшем и проверить на больших числах
# для себя сравните скорости выполнения fib_cached и fib_regular
# на больших числах (больше 60)
def fibonacci_regular(n: int) -> list:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    s = [0, 1]
    fib_1, fib_2 = 0, 1
    for i in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        s.append(fib_2)
    return s

import time
MY_CACHE: dict[str, str] = {}

def fibonacci_cached(n: int) -> list:
    if n in MY_CACHE:
        return MY_CACHE[n]
    
    if n <= 0:
        result = []
    elif n == 1:
        result = [0]
    elif n == 2:
        result = [0, 1]
    else:
        s = [0, 1]
        fib_1, fib_2 = 0, 1
        for i in range(2, n):
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            s.append(fib_2)
        result = s
    
    MY_CACHE[n] = result
    return result


try:
    n = int(input('Enter a positive integer number: '))
    if n <= 0:
        print('Error. Enter a positive integer.')
    else:
        start = time.time() #1st attempt
        seq_cached = fibonacci_cached(n)
        time_cached = time.time() - start
        
        start = time.time() #2nd attempt
        seq_cached = fibonacci_cached(n)
        time_cached = time.time() - start

        start = time.time()
        seq_regular = fibonacci_regular(n)
        time_regular = time.time() - start
        
        print(f"Sequence: {seq_cached}")
        print(f"With cache (1st attempt)): {time_cached:.6f} seconds")
        print(f"With cache (2nd attempt): {time_cached:.6f} seconds")
        print(f"Without cache: {time_regular:.6f} seconds")
        
except ValueError:
    print('Error. Enter a positive integer.')
