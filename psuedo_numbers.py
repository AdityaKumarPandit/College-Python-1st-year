# Generating Pseudo Random Numbers

# import random

# lower = int(input("Enter lower limit: "))
# upper = int(input("Enter upper limit: "))
# count = int(input("Enter number of random numbers: "))

# print("Pseudo-random numbers:")

# for _ in range(count):
#     print(random.randint(lower, upper), end=" ")
    
# Nth fibonacci series

# n = int(input("Enter n: "))

# if n < 0:
#     print("Please enter a non-negative integer.")
# elif n == 0:
#     print("Fibonacci number =", 0)
# elif n == 1:
#     print("Fibonacci number =", 1)
# else:
#     a = 0
#     b = 1

#     for _ in range(2, n + 1):
#         a, b = b, a + b

#     print("Fibonacci number =", b)
    
# Raising a Number to Large Power

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1

while exponent > 0:
    if exponent % 2 == 1:
        result *= base

    base *= base
    exponent //= 2

print("Result =", result)

