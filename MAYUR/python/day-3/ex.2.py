# Create a program that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive



def sum_divisible_by_c(a, b, c):
    divisible_sum = 0
    for num in range(a, b + 1):
        if num % c == 0:
            divisible_sum += num
    return divisible_sum

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))
c = int(input("Enter the divisor (c): "))

result = sum_divisible_by_c(a, b, c)
print("Sum of numbers divisible by", c, "from", a, "to", b, "inclusive:", result)
