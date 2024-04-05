# Create a program that takes a list of numbers and returns the sum of all prime numbers in the list.
  
  
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    prime_sum = 0
    for num in numbers:
        if is_prime(num):
            prime_sum += num
    return prime_sum


numbers_list = [3, 7, 12, 15, 20, 23]
print("Original list:", numbers_list)
print("Sum of prime numbers in the list:", sum_of_primes(numbers_list))
