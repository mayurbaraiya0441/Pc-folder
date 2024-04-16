
# Ex-4.2
# Create a function/input that counts the integer's number of digits.
# Solve this without using strings.

# Example :
# 	count(318) ➞ 3
# 	count(-92563) ➞ 5
# 	count(4666) ➞ 4
# 	count(-314890) ➞ 6
# 	count(654321) ➞ 6
# 	count(638476) ➞ 6


def count_digits(n):
    if n == 0:
        return 0
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count
count_digits(123456)
print(count_digits(123456))