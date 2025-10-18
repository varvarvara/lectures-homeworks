# task 1
# создать файл my_functions.py с функциями greet и change_name
# change_name - принимает строку, а возвращает измененное имя, где каждая вторая буква - большая
# greet - принимает строку, ничего не возвращает, а просто принтит "Hello имя" с помощью украшений из rich print

name = input('What is your name?:')

def changed_name(name: str) -> str:
    letters = list(name.lower())
    for i in range(1, len(letters), 2): #(start, stop, step)
        letters[i] = letters[i].upper()
    return ''.join(letters)

new_name = changed_name(name)

from rich import print 
def greet(new_name):
    print(f"Hello [bold blue]{new_name}[/bold blue]!")
greet(new_name)




