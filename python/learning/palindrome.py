#Method check given number palindrome or not 
n = input("Enter a input:")

def palindrome(n):
    output = ""
    if n == n[::-1] :
        print(n,"is palindrome")
    else:
        print(n,"is not palindrome")
        
palindrome(n)
