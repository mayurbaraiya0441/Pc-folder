# Finding the maximum difference between tuple pairs

# Example:

# 	Input: 
# 	tupList = [(5, 7), (2, 6), (1, 9), (1, 3)]
	
# 	Output:
# 	8






my_list_1 = [(5, 7), (2, 6), (1,9 ), (1, 3)]

print("The list of tuple is : ")
print(my_list_1)
temp_val = [abs(b - a) for a, b in my_list_1]
print(temp_val)
my_result = max(temp_val)

print("The maximum difference among tuple pairs is : ")
print(my_result)


