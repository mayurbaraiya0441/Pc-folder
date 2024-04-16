# Ex-5.5
# Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.



def nextPrime():
    num = int(input("Enter a number: "))
     
    next_num = num + 1
     
    while True:
        for i in range(2, next_num):
            if (next_num % i) == 0:
                next_num += 1
            else:
                
                break
        print(f"The next prime number is {next_num}.")
        break
nextPrime()




