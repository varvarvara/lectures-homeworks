rubles_per_pasta: float = 300.54 #рублей за единицу
rubles_per_palka: int = 150.89  #рублей за единицу
print(rubles_per_palka)

n_persons: float  = float(input("Скольким людям нужно начистить зубы?: "))

result: float = (rubles_per_palka*n_persons) + (rubles_per_pasta*(n_persons/2))

print(
    rubles_per_pasta,
    rubles_per_palka
)