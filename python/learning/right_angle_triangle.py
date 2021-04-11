#Method 1
userinput = int(input("Please enter number of line:"))

def print_star(userinput):
        for i in range(1,userinput+1):
            while i>0:
                print("*", end=" ")
                i = i-1
            print()

print_star(userinput)



#Method 2
userinput = int(input("Please enter number of line:"))

def print_star(userinput):
        for i in range(1,userinput+1):
            for j in range(1,i+1):
                print("*", end= " ")
            print()

print_star(userinput)

#Method Reverse 
rows = int(input("Please enter number of rows:"))

def reverse_righ_angle(rows):
    for i in range(rows,0,-1):
        while i>0:
            print("*", end=" ")
            i = i-1
        print()
            
reverse_righ_angle(rows)
