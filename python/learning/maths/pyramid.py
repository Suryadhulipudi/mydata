#Simple Method
def print_diamond(height):
    # Print top half of the diamond
    for i in range(1, height + 1):
        # Print spaces
        print(" " * (height - i), end="")
        # Print asterisks
        print("*" * (2 * i - 1))

    # Print bottom half of the diamond
    for i in range(height - 1, 0, -1):
        # Print spaces
        print(" " * (height - i), end="")
        # Print asterisks
        print("*" * (2 * i - 1))

# Example usage
height = 5
print_diamond(height)

#Pyramid Method
userinput = int(input("Please enter number of rows:"))

def print_pyramid(userinput):
        for i in range(0,userinput):
            for j in range(0,userinput-i-1):
                print(end=" ")
            for j in range(0,i+1):
                print("*",end=" ")
            print()

print_pyramid(userinput)

#Reverse Pyramid Method
userinput = int(input("Please enter number of rows:"))

def print_pyramid(userinput):
        for i in range(userinput,0,-1):
            for j in range(0,userinput-i):
                print(end=" ")
            for j in range(0,i):
                print("*",end=" ")
            print()

print_pyramid(userinput)

#Diamond shape
rows = int(input("Please enter number of rows:"))

def print_pyramid(rows):
        for i in range(rows):
            print(' '*(rows-i-1)+'* '*(i+1))
        for j in range(rows-1,0,-1):
            print(' '*(rows-j)+'* '*(j))
            
print_pyramid(rows)
