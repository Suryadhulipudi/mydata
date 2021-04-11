#Method 1
given_number = int(input("Enter a number:"))

def factorial(given_number):
    factorial = 1
    if given_number == 0:
        return 1
    for i in range(given_number,0,-1):
        factorial =factorial * i
    return factorial

print(factorial(given_number))

#Method 2 using inbuilt function
import math
given_number = int(input("Enter a number:"))

result = math.factorial(given_number)
print("factorial of",given_number,"is",result)

#Method 3 using recursive function
given_number = int(input("Enter a number:"))

def factorial(given_number):
    if given_number == 0:
        return 1
    else:
        return given_number*factorial(given_number-1)
      
print(factorial(given_number))
