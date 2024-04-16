# Ex-5.3
# Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.


def no_of_argu(*args):
	
	
	return(len(args))


a = 1
b = 3

n = no_of_argu(1, 2, 4, a,"hello", b)

print(" The number of arguments are: ", n)
