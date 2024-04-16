# Create a function/input that, given a number, returns the corresponding value of that index in the Fibonacci series.

# The Fibonacci Sequence is the series of numbers:

# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# Examples:
# 	fibonacci(3) ➞ 3
# 	fibonacci(7) ➞ 21
# 	fibonacci(12) ➞ 233



def Fibonacci(n):
	if n < 0:
		print("incorrect input")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(7))
