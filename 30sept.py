# 1.	Modify the square-root program to display the square root with two decimal places.

# a = int(input("Enter the Number:"))

# b = a ** 0.5

# if a < 0 :
#     print("Please Enter any positive number:")

# else:
#     print(f"Square root of {a} is {b:.4f}.")

# 2.    Generate the first n Fibonacci numbers and identify the largest Fibonacci number below a given limit.

n = int(input("Enter number: "))
a = 0 
b = 1 

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a = b 
    b = a + b
     
print(f"Largest Number = {a}")