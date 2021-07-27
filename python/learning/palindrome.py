#Method check given number palindrome(ex: 121, 242) or not 
n = input("Enter a input:")

def palindrome(n):
    output = ""
    if n == n[::-1] :
        print(n,"is palindrome")
    else:
        print(n,"is not palindrome")
        
palindrome(n)

#Method to print palindrome numbers
start = 0
end = 500

def palindrome(start,end):
    for i in range(start, end+1):
        i = str(i)
        if i == i[::-1]:
            print(i,"is palindrome")
        else:
            print(i,"is not palindrome")
            
palindrome(start,end)

#Method to print without function

num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")


#Method for any string type
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "121"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")
