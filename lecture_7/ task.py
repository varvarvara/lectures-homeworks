#Shrek, PussInBoots, Donkey, JackHorner
#на каждого должен быть и персонаж, и фанко поп, и косплеер
#итого должно быть:
#BaseCharacter: Shrek PussInBoots Donkey JackHorner
#BaseCharacter -> BaseInActionCharacter: Shrek -> ShrekInAction PussInBoots -> PussInBootsInAction Donkey -> DonkeyInAction JackHorner -> JackHornerInAction
#BaseCharacter -> BaseFunkoPop: Shrek -> ShrekInAction PussInBoots -> PussInBootsInAction Donkey -> DonkeyInAction JackHorner -> JackHornerInAction
#BaseCharacter -> BaseCosplayer <- BaseHuman: Shrek -> ShrekCosplayer PussInBoots -> PussInBootsCosplayer Donkey -> DonkeyCosplayer JackHorner -> JackHornerCosplayer

from abc import abstractmethod
from typing import override

#mixins to BaseCharacter
class MixinSpeakable:
    def speak(self):
        print(f"{self.name} говорит что-то!")

class MixinAnimated:
    def __init__(self, is_animated: bool):
        self.is_animated = is_animated

class MixinFunny:
    def make_laugh(self):
        print(f"{self.name} делает что-то смешное!")
    
import random

character_names = ["Shrek", "Donkey", "Puss in Boots", "Jack Horner"]

class BaseCharacter(MixinSpeakable, MixinAnimated, MixinFunny):
    def __init__(self, name=None, is_animated=True):
        if name is None:
            name = random.choice(character_names)
        
        MixinAnimated.__init__(self, is_animated)
        self.name = name
        
#Main characters
class Shrek(BaseCharacter):
    def __init__(self):
        super().__init__("Shrek")

class PussInBoots(BaseCharacter):
    def __init__(self):
        super().__init__("Puss in Boots")

class Donkey(BaseCharacter):
    def __init__(self):
        super().__init__("Donkey")

class JackHorner(BaseCharacter):
    def __init__(self):
        super().__init__("Jack Horner")
        
#In action characters
class MixinActionable: 
    def perform_action(self):
        return f"{self.name} выполняет множество действий!"

class BaseInActionCharacter(BaseCharacter, MixinActionable):
    def __init__(self, name: str, is_animated: bool = True):
        BaseCharacter.__init__(self, name, is_animated)
        
class ShrekInAction(BaseInActionCharacter, Shrek):
    pass
    
class PussInBootsInAction(BaseInActionCharacter, PussInBoots):
    pass    
    
class DonkeyInAction(BaseInActionCharacter, Donkey):
    pass

class JackHornerInAction(BaseInActionCharacter, JackHorner):
    pass


#Collecteable characters

class MixinCollectable:
    def is_collectable(self):
        if self.is_collectable:
            return f"{self.name} можно собрать!"
        else:
            return f"{self.name} нельзя собрать!"
    
    
class FunkoPop(MixinCollectable, BaseCharacter):
    def display(self):
        return f"{self.name} представлен на FunkoPop!"
    
class ShrekFunckoPop(FunkoPop, Shrek):
    pass

class PussInBootsFunckoPop(FunkoPop, Shrek):
    pass

class DonkeyFunckoPop(FunkoPop, Shrek):
    pass

class JackHornerFunckoPop(FunkoPop, Shrek):
    pass


#Cosplay characters
class BaseHuman:
    def __init__(self, human_name):
        self.human_name = human_name


class MixinPoseable:
    def pose(self):
        return f"{self.name} встает и делает что-то смешное!"

class MixinCostumeWearable:
    costume: str
    
class BaseCosplayer(BaseHuman, MixinPoseable, MixinCostumeWearable):
    def __init__(self, human_name, costume):
        BaseHuman.__init__(self, human_name)
        BaseCharacter.__init__(self, self.name) # надо проверить этот пункт
        
        
class ShrekCosplayer(BaseCosplayer):
    pass

class PussInBootsCosplayer(BaseCosplayer):
    pass

class DonkeyCosplayer(BaseCosplayer):
    pass

class JackHornerCosplayer(BaseCosplayer):
    pass


if __name__ == "__main__":
    character = BaseCharacter()
    print(f"Character: {character.name}")
    character.speak()
    character.make_laugh()
    print(f"Is animated? {character.is_animated}")
    print.pose()
    # print(f"{character.is_collectable}")
    

