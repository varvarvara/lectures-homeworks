name: str = "Ilya"



for i in range(1, 5+1, 2):
    print(
        f"Hello {name}=! {i}"
        )
    
#lazy functions

sentence: str = "Hello Bob! How are you?"
splitted_sentence: list[str] = sentence.split()
print(splitted_sentence)

for value in splitted_sentence:
    if len(value) == 3:
        print(f"We found {value =} with len={len(value)} ")

        