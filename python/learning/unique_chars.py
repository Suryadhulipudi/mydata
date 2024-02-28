# Method-1
def find_unique_chars(input_string):
    # Initialize an empty set to store unique characters
    unique_chars = set()

    # Iterate through each character in the input string
    for char in input_string:
        # Add the character to the set if it's not already present
        unique_chars.add(char)

    # Return the set containing unique characters
    return unique_chars

# Example usage
input_string = "hello"
unique_chars = find_unique_chars(input_string)
print("Unique characters:", unique_chars)

# Method-2
String = "prepinsta"
for i in String:
    #initialize a count variable
    count = 0
    for j in String:
        #check for repeated characters
        if i == j:
            count+=1
        #if character is found more than 1 time
        #brerak the loop
        if count > 1:
            break
    #print for nonrepeating characters
    if count == 1:
        print(i,end = " ")

# Method-3
def firstNonRepeatingChar(str1):
   char_order = []
   counts = {}
   for c in str1:
      if c in counts:
         counts[c] += 1
      else:
         counts[c] = 1
         char_order.append(c)
   for c in char_order:
      if counts[c] == 1:
      return c
   return None

print(firstNonRepeatingChar('PythonforallPythonMustforall'))
print(firstNonRepeatingChar('tutorialspointfordeveloper'))
print(firstNonRepeatingChar('AABBCC'))


        

