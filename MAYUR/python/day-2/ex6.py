# A fruit juice company tags their fruit juices by concatenating the first three letters of the words in a flavor's name, with its capacity.

# Create a Program that creates product IDs for different fruit juices.

# Example :
# 	("apple", "500ml") ➞ "APP500"

# 	("pineapple", "45ml") ➞ "PIN45"

# 	("passion fruit", "750ml") ➞ "PASFRU750"


id1="apple 500ml"
id2="pineapple 45ml"
id3="passion fruit 750ml"



capacity=id1.replace("ml","").split()[1]
# print(capacity,'capacity')

fruit=id1.split()[0][0:3]
print(f"apple, 500ml ➞ {fruit.upper()}{capacity}")



p=id2.replace("ml","").split()[1]
# print(p,'p')

app=id2.split()[0][0:3]
print(f"pineapple, 45ml ➞ {app.upper()}{p}")




it=id3.split()[0][0:3]
# print(it)

a=id3.split()[1][0:3]
# print(a)


fru=id3.replace("ml","").split()[2]
# print(fru,'fru')


print(f"passion fruit, 750ml ➞ {it.upper()}{a.upper()}{fru}")







