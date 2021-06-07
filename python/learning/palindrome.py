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
