#Method print prime numbers
start = 0
end = 25

def prime_numbers(start,end):
    for i in range(start, end+1):
        if i>1:
            for j in range(2,i):
                if(i % j==0):
                    break
            else:
                print(i)
                
prime_numbers(start,end)
    
#Check given number is prime or not
num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0: 
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  
