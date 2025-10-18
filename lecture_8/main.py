import random
from enum import StrEnum
from threading import ExceptHookArgs
from typing import Self

from rich.console import Console
from rich.table import Table

console = Console()

class Names(StrEnum):
    JOHN = "John Lennon"
    PAUL = "Paul McCartney"
    GEORGE = "George Harrison"
    RINGO = "Ringo Starr"


class Beetle:
    health_points: int
    name: Names

    def __init__(
        self,
        health_points: int = 100,
        max_health_points: int = 100,
        name: Names = Names.JOHN,
    ) -> None:
        self.health_points = health_points
        self.max_health_points = max_health_points
        self.name = name

    def __eq__(self, other: Self) -> bool:
        return self.health_points == other.health_points

    def __lt__(self, other: Self) -> bool:
        return self.health_points < other.health_points

    def __le__(self, other: Self) -> bool:
        return self.health_points <= other.health_points

    def __str__(self) -> str:
        return f'Beetle(name="{self.name}", hp={self.health_points!r})'

    def styling(self) -> str:
        if self.name is Names.JOHN:
            return "in Johny style"
        elif self.name is Names.PAUL:
            return "in McCartney style"
        return "without style"

    def alive(self): 
        return self.hp > 0

    def attack(self, other: Self) -> None:
        damage = 10
        other.health_points -= damage
        console.print(f"[red]{self.name}[/red] attacks [blue]{other.name}[/blue] for {damage} damage")
        if other.health_points <= 0:
            other.health_points = 0
            console.print(f"[blue]{other.name}[/blue] died!")
            self.health_points = min(self.max_health_points, self.health_points + 10)
            console.print(f"[red]{self.name}[/red] rewarded with {10} health points")
            
class BeetlesArmy:
    beetles_list: list[Beetle]
    beetles_name: Names
    beetles_max_health_points: int

    def __init__(
        self,
        beetles_name: Names,
        beetles_army_size: int = 20,
        beetles_max_health_points: int = 100,
    ):
        self.beetles_list = []
        self.beetles_name = beetles_name
        self.beetles_max_health_points = beetles_max_health_points

        for _ in range(beetles_army_size):
            beetle = Beetle(
                health_points=random.randint(1, self.beetles_max_health_points),
                name=self.beetles_name,
            )
            self.beetles_list.append(beetle)

    def __len__(self) -> int:
        return len(self.beetles_list)

    def __add__(self, other: Self) -> Self:
        if self.beetles_name != other.beetles_name:
            raise ValueError("Cannot make two different-named beetles friends")
        new_beetles_list: list[Beetle] = self.beetles_list + other.beetles_list
        new_army = self.__class__(
            beetles_army_size=1,
            beetles_name=self.beetles_name,
            beetles_max_health_points=self.beetles_max_health_points,
        )
        new_army.beetles_list = new_beetles_list
        return new_army

    def print_army_listing(self):
        for beetle in self.beetles_list:
            print(beetle)
            
    def alive_beetles(self):
        return [beetle for beetle in self.beetles_list if beetle.health_points > 0] #возвращает список со всеми выжившими
        
    def is_defeated(self) -> bool:
        return len(self.alive_beetles()) == 0
        
    def attack(self, other: Self):
        self.beetles_list[0].attack(other.beetles_list[0])

        if other.beetles_list[0].health_points <= 0:
            other.beetles_list[0].health_points = 0
            self.beetles_list[0].health_points += 10  # reward
            other.beetles_list.pop(0)
    
        other.beetles_list[0].attack(self.beetles_list[0])
        
        if self.beetles_list[0].health_points <= 0:
            self.beetles_list[0].health_points = 0
            other.beetles_list.pop(0) #убираем
        
    
    def battle(self, other: Self):
        round_num = 1
        while self.alive_beetles() and other.alive_beetles():
            console.print(f"\n--- Round {round_num} ---")
            self.attack(other)
            round_num += 1

        if self.total_health() > other.total_health():
            console.print(f"\n[bold green]{self.beetles_name.value} wins![/bold green]")
        elif self.total_health() < other.total_health():
            console.print(f"\n[bold red]{other.beetles_name.value} wins![/bold red]")
        else:
            console.print("\n[bold yellow]It's a tie![/bold yellow]")

    def total_health(self):
        return sum(beetles.health_points for beetles in self.beetles_list)

    # Army comparisons
    def __gt__(self, other: Self):
        return self.total_health() > other.total_health()

    def __lt__(self, other: Self):
        return self.total_health() < other.total_health()

    def __eq__(self, other: Self):
        return self.total_health() == other.total_health()

if __name__ == "__main__":
    warrior_1 = Names[input("Enter first army name (JOHN/PAUL/GEORGE/RINGO): ").upper()]
    num_1 = int(input("Enter first army size: "))

    warrior_2 = Names[input("Enter second army name (JOHN/PAUL/GEORGE/RINGO): ").upper()]
    num_2 = int(input("Enter second army size: "))

    if warrior_1 == warrior_2:
        print("Both armies have the same name! Try again.")
        exit()
    
    army1 = BeetlesArmy(beetles_name=warrior_1, beetles_army_size=num_1)
    army2 = BeetlesArmy(beetles_name=warrior_2, beetles_army_size=num_2)

    print('ARMY 1')

    army1.print_army_listing()
    print('')
    
    print('ARMY 2')
    army1.print_army_listing()
    print('')
    
    army1.battle(army2)
    
    
    # m1 = Beetle(health_points=90, name=Names.JOHN)
    # m2 = Beetle(health_points=90, name=Names.PAUL)
    # print("==", m1 == m2)
    # print("!=", m1 != m2)
    # print("<", m1 < m2)
    # print(">", m1 > m2)
    # print("<=", m1 <= m2)
    # print(">=", m1 >= m2)

    # print(m1, str(m2))

    # print("ARMY 1:")
    # ba1 = BeetlesArmy(
    #     beetles_name=Names.PAUL,
    #     beetles_army_size=10,
    #     beetles_max_health_points=30,
    # )
    # ba1.print_army_listing()
    # print()

    # print("ARMY 2:")
    # ba2 = BeetlesArmy(
    #     beetles_name=Names.JOHN,
    #     beetles_army_size=10,
    #     beetles_max_health_points=30,
    # )
    # ba2.print_army_listing()
    # print()

    # # LBYL
    # if ba1.beetles_name == ba2.beetles_name:
    #     ba3 = ba1 + ba2
    #     print("ARMY 3:")
    #     ba3.print_army_listing()
    #     del ba1, ba2
    # else:
    #     print("You stooopid")

    # EAFP
    # try:
    #     ba3 = ba1 + ba2
    #     print("ARMY 3:")
    #     ba3.print_army_listing()
    #     del ba1, ba2
    # except ValueError as ex:
    #     print(f"You stooopid: {ex}")
    # except TypeError as ex:
    #     print("Typing is stoopid")
        
    

# Задание:
#
# Продолжить логику битв армий жуков
# Где каждая армия бьёт другую по очереди
# пока у неё не закончатся жуки
#
# Жук умирает при здоровье <= 0
# Жук получает +10 хп за убийство жука, но не больше своего max_hp в армии
#
# Весь прогресс битвы можно красиво выводить с помощью rich
#
# Должен быть функционал сравнения армий
# Все данные о битве (сколько армий и под каким именем) - запрашивайте у пользователя
# Урон должен быть определен так же как и ХП, но при .attack() варьироваться каждый раз от рандомdef attack(self):J