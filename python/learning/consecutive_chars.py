# Python 3 program to print run
# length encoding of a string

#Method-1 
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
 
#Method-2
def find_repetitive_chars(string):
    char_counts = {}
    repetitive_chars = []

    # Count occurrences of each character
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Find repetitive characters
    for char, count in char_counts.items():
        if count > 1:
            repetitive_chars.append(char)

    return repetitive_chars

if __name__ == "__main__":
    string = "hello world"
    result = find_repetitive_chars(string)
    print("Repetitive characters found:", result)

