sentence = input("Enter the sentence:")
string = sentence.lower()
count = 0

list = ["a","e","i","o","u"]

for char in string:
    if char in list:
        count = count + 1

print("Number of vowels in given sentence is:", count)
