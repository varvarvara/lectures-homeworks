from abc import abstractmethod
from typing import override

class BaseDuck:
    wings: int = 2
    beak: bool = True
        
class MixinNoisable: 
    @abstractmethod
    @override
        
    def make_noise(self, volume_db: int) -> None:
        raise NotImplementedError
    
class MixinDustable:
    def get_dusty(self) -> None:
        print("get dusty")
        
class MixinWalkable:
    legs: int = 2
    

class Duckess(BaseDuck, MixinNoisable, MixinDustable, MixinWalkable):
    def make_noise(self, volume_db: int) -> None:
        print(f"quackie ({volume_db} DB)")

class Duck(BaseDuck, MixinNoisable, MixinDustable, MixinWalkable):
    def make_noise(self, volume_db: int) -> None:
        print(f"quackie ({volume_db} DB)")

class BaseToy():
    material: str = "plastic"
    
class ToyDuck(BaseDuck, BaseToy):
    def make_noise(self, volume_db: int) -> None:
        print(f"bizz ({volume_db: int} DB)")
        

if __name__ == "__main__":
    d1 = Duck()
    d1.make_noise(12)