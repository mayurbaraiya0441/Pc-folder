# Ex-7.4
# i) Write a program to read json file and show in terminal.
# ii) Write a program to dump/write data in json file.



# Python program to read
# json file

# import json


# f = open('data.json')


# data = json.load(f)


# for i in data['emp_details']:
# 	print(i)


# f.close()


#write in jsonfile

import json
from demo import a

print(a)

dictionary = {
	"name": "ronak",
	"rollno": 12,
	"cgpa": 8.6,
	"phonenumber": "8400001111"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sampl.json
with open("dataas.json", "w") as outfile:
	outfile.write(json_object)



