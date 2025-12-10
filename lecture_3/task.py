# дан регион [-1000, 1000]
# пользователь загадал любое целое число

# задача программы замучить поль пользователя вопросами в виде:
# взять середину региона и спросить больше или меньше выбранного числа
# и так в цикле делить регион пополам, сужая область поиска
# пока не найдём нужное число 

n_list = []

high = int(input("Put the highest threshold of the list: "))
low = int(input("Put the the lowest thershold of the list: "))

n_list = list(range(low, high + 1))

# print(n_list[0])
# print(len(n_list))
# print(n_list[-1])
# print(n_list)

new_high, new_low = high, low

while new_low <= new_high:
    middle = (new_high + new_low) // 2
    
    print("The middle one in the created list is", middle)
    
    user_input =  input("Is your number bigger (>), smaller (<) or equal (=) to the middle one? \n If you don't want to continue - print exit:").strip() 

    if user_input == "=":
        print ("Your number is", middle)
        break

    elif user_input == ">":
        new_low = middle + 1
        
    elif user_input == "<":
        new_high = middle - 1
        
    elif user_input.lower == "exit":
        print("Exit")
        exit()
        
    else:
        print("I will repeat for you again\n Is your number bigger (>), smaller (<) or equal (=) to the middle one?:")
        
if new_low > new_high:
    print("Something went wrong! Check your answers.")
    

