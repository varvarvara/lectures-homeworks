# Запросить у пользователя - хочет ли он сняться в кино
# Если да - предложить две разных роли - Халк или Локи
#   Если халк - запросить сколько у него бицепс в объеме
#       Если меньше 60 - отправить домой
#       Еслиб больше или равно - сказать что он принят
#   Если локи - спросить кого он больше любит - маму или папу
#       Если папу - отправить домой
#       Если маму - отправить к папе, чтобы спросил кого больше любит
# Если нет - попрощаться
# Во всех условиях обрабатывать белиберду и неправильные выборы ошибкой для пользователя


desire: str = input("Do you want to be an actor in a film?[Yes/No]:")

if desire.lower() == "yes":
    role: str = str(input("Do you want to play Halk or Loki?"))
    if role == "Halk":
        biceps = input("What is the size of your biceps? (put a number):")
        if biceps.isdigit():
            if biceps < 60:
                print("Go home, man...")
            elif biceps >= 60:
                print("You are in, man.")
        else:
            print("Don't use the word")
    elif role == "Loki":
        parent: str = str(input("Who is your favourite parent: mom or dad?"))
        if parent == "dad":
            print("Go home")
        elif parent == "mom":
            print("Go to dad and ask him whom you should love more...")
        else:
            print("You have only two variants...")
elif desire.lower() == "no":
    print("Bye and go to hell!")
else:
    print("Stupid bitch...")