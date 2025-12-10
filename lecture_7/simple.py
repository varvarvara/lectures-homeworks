class Human: #naming for classes - all words starting with capital letters
    name: str
    eyes: int
    hands: int 
    legs: int
    hair_color: str = "brown"
    
    def __init__(
        self,
        name: str="Vova", 
        hands: int = 2, 
        legs: int=2,
        eyes: int = 2
        ): #вынуждены перенести в нэйм и лэгс в значения
        self.name = name
        self.legs = legs
        self.hands = hands
        self.eyes = eyes
        
    
    def blink(self):
        print(f"{self.name} blinked")
        
    def walk(self): #self - ссылка на класс
        print(f"{self.name} walked away")
        
    def do_nothing():
        print("nothing happend")
        
    def break_plank(self, plank_material = "wooden", quantity: int = 2):
        print(
            f"Breaks {quantity} {plank_material} planks"
            )
        
class SmartHuman(Human):
    glasses: bool = True
    iq: int = 130
    
    def __init__(self, glasses: bool = True, iq: int = 130):
        super().__init__()
        self.glasses = glasses
        self.iq = iq
    
    def blink(self):
        print(
            f"Smart {self.name} blinked with {self.eyes} "
            f"and with glasses {'on' if self.glasses else 'off'}"
        )


if __name__ == "__main__":
   human1 = Human()
   
   human1.blink()
   human1.break_plank()
   human1.break_plank("plastic", 3)
   
   human2 = Human(name="Aundrey", legs=2)
   human2.blink()
   
   smart_human1 = SmartHuman()
   smart_human1.blink()
   
   

    
    