#Print perfect numbers, sum of divisors = give number
start = 0
end = 500


def perfect_numbers(start,end):
    for i in range(start, end+1):
        temp = 0
        for x in range(1,i):
            if(i%x == 0):
                temp = temp + x
        if (temp == i) and i!=0:
            print(i)
            
perfect_numbers(start,end)


#Check given number is perfect or not
n = int(input("Enter a number:"))


def perfect_numbers(n):
    temp = 0
    for x in range(1,n):
        if(n%x == 0):
            temp = temp + x
    if (temp == n) and n!=0:
        print(n,"is perfect number")
          
    else:
        print(n,"is not perfect number")
perfect_numbers(n)



