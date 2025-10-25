# task 1
# создать файл my_functions.py с функциями greet и change_name
# change_name - принимает строку, а возвращает измененное имя, где каждая вторая буква - большая
# greet - принимает строку, ничего не возвращает, а просто принтит "Hello имя" с помощью украшений из rich print

import rich
from rich import print

def change_name(name: str) -> str:
    letters = list(name.lower())
    for i in range(1, len(letters), 2): #(start, stop, step)
        letters[i] = letters[i].upper()
    return ''.join(letters)

def greet(name: str) -> None:
    print(f"[bold cyan]Hello[/bold cyan] [bold magenta]{name}[/bold magenta]!")

name = input('What is your name?: ')
changed_name = change_name(name)
greet(changed_name)




