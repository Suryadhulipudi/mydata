#Method-1
def print_right_angle_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

# Example usage
height = 5
print_right_angle_triangle(height)


#Method 2
userinput = int(input("Please enter number of line:"))

def print_star(userinput):
        for i in range(1,userinput+1):
            while i>0:
                print("*", end=" ")
                i = i-1
            print()

print_star(userinput)



#Method 3
userinput = int(input("Please enter number of line:"))

def print_star(userinput):
        for i in range(1,userinput+1):
            for j in range(1,i+1):
                print("*", end= " ")
            print()

print_star(userinput)

#Method Reverse-1
def print_reverse_right_angle_triangle(height):
    for i in range(height, 0, -1):
        print('*' * i)

# Example usage
height = 5
print_reverse_right_angle_triangle(height)

#Method Reverse-2
rows = int(input("Please enter number of rows:"))

def reverse_righ_angle(rows):
    for i in range(rows,0,-1):
        while i>0:
            print("*", end=" ")
            i = i-1
        print()
            
reverse_righ_angle(rows)
