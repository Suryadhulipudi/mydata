user_input = int(input("Fibonancci series upto:"))

def fibonancci(user_input):
    a = 0
    b = 1
    count = 0
    if user_input <= 0:
        print("Please enter a positive number")
    elif user_input == 1:
        print("Fibonancci terms", a)
    else:
        while count < user_input:
            print(a)
            c = a + b
            a = b
            b = c
            count += 1

fibonancci(user_input)
    
