#Reverse string 
def rev(str):
    return str[::-1]
    
user_input = input("Enter the input:")
print(rev(user_input))

#Reverse list with reverse function
def rev(user_input):
    user_input.reverse()
    return user_input
    
user_input = ["acds","sdfsd","zzz","yy"]
print(rev(user_input))

#Reverse list with reversed function
def rev(user_input):
    out = reversed(user_input)
    return out
    
user_input = ["acds","sdfsd","zzz","yy"]
print(list(rev(user_input)))

#Reverse a list without any function
def rev(user_input):
    leng = len(user_input)
    for i in range(leng//2):
        temp = user_input[i]
        user_input[i] = user_input[leng-i-1]
        user_input[leng-i-1]=temp
    return user_input
    
user_input = ["acds","sdfsd","zzz","yy"]
print(rev(user_input))


