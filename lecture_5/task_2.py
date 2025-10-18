#Fibonacci sequence


n = int(input("Put an integer number: "))

def fibonacci(n: int) -> int:
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
    return s
    
seq = fibonacci(n)
print(seq[-1])




