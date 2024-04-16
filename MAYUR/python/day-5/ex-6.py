# Ex-5.6
# Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.




myDict = {'rajvi': 10, 'rajnish': 9,
		'sanjeev': 15, 'yash': 2, 'suraj': 32}

myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}

print(sorted_dict)
