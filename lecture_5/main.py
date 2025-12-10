
x = 0 #заглавные буквы - константа (не должно быть счёта)

def print_to_console(): #не использовать в начале функции цифры и спецсимволы
    global x #найти функцию ранее
    x += 1
    print('Hello', x)
    x += 1
    
print_to_console()
print_to_console()
print_to_console()
