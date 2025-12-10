import time

# print('Hello')
# time.sleep(3)
# print('world')

import time
from functools import lru_cache

@lru_cache()

def calculate_greeting(age: int, name: str = 'Vova') -> str: #Vova - default
    wait_time = 5
    print (f"waiting {wait_time} seconds...")
    time.sleep(wait_time)
    print("I am awake")
    return f"Hello {name} ({age} y.o.)"

# if __name__ == '__main__':
#     _ = calculate_greeting(name ="Ilya", age = 18)
#     print(calculate_greeting(name ="Ilya", age = 18))

MY_CACHE: dict[str,str] = {}
def calculate_surname(name: str = "Vova"):
    if name in MY_CACHE.keys():
        return MY_CACHE[name]
    time.sleep(5)
    surname = "Vova" + "4kin"
    MY_CACHE[name]= surname
    return surname
    
print(f"{MY_CACHE} = ")
print(
    calculate_surname("Ilya")
)

print(
    calculate_surname("")
)

print(
    calculate_surname("Ilya")
)
print(
    calculate_surname("Andrey")
)
        
        
        
    