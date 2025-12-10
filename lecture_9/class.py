import random
from enum import StrEnum
from threading import ExceptHookArgs
from typing import Self

class Names(StrEnum):
    JOHN: str  = "John Lennon"
    PAUL: str = "Paul McCartney"
    GEORGE: str = "George Harrison" 
    RINGO: str = "Ringo Starr"


class Beatles:
    health_points:int
    name: Names
    damage:int
    
    
    def __init__(self, health_points: int, damage: int, name: Names = Names.JOHN):
        self.health_points = health_points
        self.damage = damage
        self.name = name
        
    
    def __eq__(self, other) -> bool:
        return self.health_points == other.health_points

    def __str__(self): #это dunder, который отвечает за строковое представление объекта
        return f"Beatle(name={self.name}, hp={self.health_points}, dmg={self.damage})"
    
    def __lt__(self, other: Self) -> bool:
        return self.health_points < other.health_points

    def __le__(self, other: Self) -> bool:
        return self.health_points <= other.health_points


    def styling(self) -> str:
        if self.name is Names.JOHN:
            return "in Johny style"
        elif self.name is Names.PAUL:
            return "in McCartney style"
        return "without style"
    
    def attack(self, other: "Beatles"):
        if self.health_points <= 0:
            return 0  # мёртвый не атакует

        damage_dealt = random.randint(1, max(1, self.damage))
        other.health_points -= damage_dealt

        print(
        f"{self.name} attacked {other.name} {self.styling()} "
        f"and dealt {damage_dealt} dmg (target hp -> {max(other.health_points, 0)})" #переписать формулровку
    )

        if other.health_points <= 0:
            print(f"{other.name} has fallen!")
            self.health_points = min(self.health_points + 10, 100)
            print(f"{self.name} gains +10 HP (now {self.health_points})")

class BeatlesArmy:
    beatles_list: list[Beatles]
    beatles_name: Names
    beatles_max_health_points: int
    
    def __init__(
        self,
        beatles_name: Names,
        beatles_army_size: int = 20,
        beatles_max_health_points: int = 100,
    ):

        self.beatles_list = []
        self.beatles_name = beatles_name
        self.beatles_max_health_points = beatles_max_health_points


        for _ in range(beatles_army_size):
            beatle = Beatles(
                health_points=random.randint(1, self.beatles_max_health_points),
                name=self.beatles_name,
            )
            self.beatles_list.append(beatle)
            
    def __len__(self):
        return len(self.beatles_list)
    
    def __add__(self,other: Self):
        if self.beatles_name != other.beatles_name:
            raise ValueError("Cannot make different Beatles friends")
        new_beatles_list: list[Beatles] = self.beatles_list + other.beatles_list
        new_army = self.__class__(
            beatles_name = self.beatles_name,
            beatles_max_health_points = self.beatles_max_health_points
        )
        new_army.beatles_list = new_beatles_list
        return new_army
    
    def print_army_listing(self):
        for beatle in self.beatles_list:
            print(beatle)
            
    def attack (self, target):
        target.hp -= self.damage
        target.hp = max(target.hp,0)


    while True:
        self.beatles.attack()
        other.beatles.attack()
        
    
if __name__ == "__main__":
    # m1: Beatles = Beatles(health_points =100, name = Names.JOHN)
    # m2: Beatles = Beatles(health_points = 100, name = Names.PAUL)
    # # print(m1.name)
    # # print(f"{m2.health_points} health points left")
    # # m1.attack(other=m2)
    # print(m1 == m2)
    # print(m1, m2  )

    print('ARMY 1:')

    ba1: BeatlesArmy = BeatlesArmy(
        beatles_name = Names.PAUL,
        beatles_army_size = 9,
        beatles_max_health_points = 30
    )
    ba1.print_army_listing()
    print()

    print('ARMY 2:')

    ba2: BeatlesArmy = BeatlesArmy(
        beatles_name = Names.JOHN,
        beatles_army_size = 10,
        beatles_max_health_points = 100
    )
    ba2.print_army_listing()
    print()
    
    
    try:
        ba3 = ba1 + ba2
        print("ARMY 3:")
        ba3.print_army_listing()
        del ba1, ba2
    except ValueError as ex:
        print(f"You stooopid: {ex}")
    except TypeError as ex:
        print("Typing is stoopid")


#del ba1, ba2
#LBYL - look before you leap (==)

    



