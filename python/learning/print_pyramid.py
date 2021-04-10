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
