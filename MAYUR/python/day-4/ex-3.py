# Given a list nums where each integer is between 1 and 100, return a sorted list containing only duplicate numbers from the given nums list

# Examples:
# 	duplicate_nums([1, 2, 3, 4, 3, 5, 6]) ➞ [3]
# 	duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]) ➞ [72, 81, 99]
# 	duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ None



list=[1, 2, 3, 4, 3, 5, 6]


uniqueList = []
duplicateList = []
 
for i in list:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)
 
print(duplicateList)



