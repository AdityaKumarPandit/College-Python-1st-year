numbers = [10, 20, 30, 40, 50]

print(numbers)
print(numbers[0])       # first element
print(numbers[-1])      # last element
print(len(numbers))     # number of elements 

# Reversing of the Array

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

numbers = [10, 20, 30, 40, 50]
print("Original:", numbers)
print("Reversed:", reverse_array(numbers))

# Array reverse in simpler way

numbers = [10, 20, 30, 40, 50]
print(numbers)
numbers.reverse()
print(numbers)

# Number Counting  in array :)

def count_value(arr, target):
    count = 0

    for value in arr:
        if value == target:
            count += 1

    return count

numbers = [2, 5, 2, 8, 2, 9, 5]
print("Count of 8 =", count_value(numbers, 8))

# Maximum in Array 

def find_maximum(arr):
    maximum = arr[0]

    for value in arr[1:]:
        if value > maximum:
            maximum = value

    return maximum

numbers = [18, 5, 42, 11, 27]
print("Maximum =", find_maximum(numbers))

# Removing duplicates in an array (BASIC WALA)

def remove_duplicates_sorted(arr):
    if not arr:
        return []

    write = 1

    for read in range(1, len(arr)):
        if arr[read] != arr[write - 1]:
            arr[write] = arr[read]
            write += 1

    return arr[:write]

numbers = [1, 1, 2, 2, 2, 3, 4, 4, 5]
print(remove_duplicates_sorted(numbers))

# 

# Pivot - Middle value when the numbers are arrange in ascending order.

def partition(arr, pivot):
    smaller = []
    greater_or_equal = []

    for value in arr:
        if value < pivot:
            smaller.append(value)
        else:
            greater_or_equal.append(value)

    return smaller + greater_or_equal

numbers = [9, 3, 7, 2, 8, 4, 6]
print(partition(numbers, 6))

# Sort the values in ascending order.
# Convert k to a zero-based index using k-1.
# Return the value at that index.

def kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k is out of range")

    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]

numbers = [7, 2, 9, 4, 1, 6]
print("Sorted:", sorted(numbers))
print("3rd smallest:", kth_smallest(numbers, 3))

# Reverse an array without using reverse() or slicing.

def reverse_array(array):
    
    A =[]
    
    for i in range(len(array)):
        A.append(array[-1*(i+1)])

    return A

numbers = [10,20,30,40]
print(reverse_array(numbers))
