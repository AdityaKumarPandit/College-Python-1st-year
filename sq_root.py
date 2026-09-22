n = int(input("Enter a positive integer: "))

if n < 0:
    print("Square root is not defined for a negative number.")
else:
    i = 0
    while i * i <= n:
        i += 1
    print("Integer square root =", i - 1)