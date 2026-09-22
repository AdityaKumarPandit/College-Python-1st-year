# n = int(input("Enter a positive integer: "))

# if n < 0:
#     print("Square root is not defined for a negative number.")
# else:
#     i = 0
#     while i * i <= n:
#         i += 1
#     print("Integer square root =", i - 1)

# Smallest divisor 🥀😭

# n = int(input("Enter an integer greater than 1: "))

# divisor = 10

# while divisor <= n:
#     if n % divisor == 0:
#         break
#     divisor += 1

# print("Smallest divisor =", divisor)

# Greatest Common Divisor 😎😏

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)