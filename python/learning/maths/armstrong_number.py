#Armstrong number(The digit numbers equal to the sum of the powers of their digits ex: 1^3+5^3+3^3 = 153)
given_number = int(input("Enter a number:"))

def armstrong(given_number):
    sum = 0
    n  = len(str(given_number))
    while given_number >0:
        que = given_number%10
        print(que)
        sum = sum + (que**int(n))
        given_number = given_number//10
    return sum


if armstrong(given_number) == given_number:
    print("%d is an armstrong number" %(given_number))
else:
    print(given_number, "is not an armstrong number")
