# Python 3 program to print run
# length encoding of a string
 
def printRLE(s) :
 
    i = 0
    while( i < len(s) - 1) :
 
        # Counting occurrences of s[i]
        count = 1
 
        while s[i] == s[i + 1] :
 
            i += 1
            count += 1
             
            if i + 1 == len(s):
                break
         
        print(str(s[i]) + str(count),  
                          end = "")
        i += 1
     
    print()
 
# Driver Code
if __name__ == "__main__" :
 
    # function calling
    printRLE("GeeeEEKKKss")
    printRLE("cccc0ddEEE")
 
