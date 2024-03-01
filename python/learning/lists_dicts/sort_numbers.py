#Method-1
NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for i in range (Number):
    for j in range(i + 1, Number):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp

print("Element After Sorting List in Ascending Order is : ", NumList)

# Method-2
def sort_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers

# Example usage
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sort_numbers(numbers)
print("Sorted numbers:", sorted_numbers)

# Method3
def sort_numbers(numbers):
    numbers.sort()
    return numbers

# Example usage
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sort_numbers(numbers)
print("Sorted numbers:", sorted_numbers)

