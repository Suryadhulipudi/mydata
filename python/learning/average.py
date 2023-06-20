#Method:1
# Python program to get average of a list
def Average(lst):
	return sum(lst) / len(lst)

# Driver Code
lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)

# Printing average of the list
print("Average of the list =", round(average, 2))

#Method:2
# Python code to get average of list
def Average(lst):
	sum_of_list = 0
	for i in range(len(lst)):
		sum_of_list += lst[i]
	average = sum_of_list/len(lst)
	return average


# Driver Code
lst = [15, 9, 55, 41, 35, 20, 62, 49]
average = Average(lst)
print("Average of the list =", round(average, 2))
