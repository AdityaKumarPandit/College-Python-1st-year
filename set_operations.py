# Basic Sets Functions in Python.

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# print("Union:", A | B)
# print("Intersection:", A & B)
# print("A - B:", A - B)
# print("B - A:", B - A)
# print("Symmetric difference:", A ^ B)

# A.add(7)
# A.remove(1)
# print(A)

# C = {0,1,2,3}

# print("Union:", A | C | B)
# print("Intersection:", A & C & B)
# print("A - C - B:", A - C - B)
# print("C - A - B:", C - A - B)
# print("Symmetric difference 1:", B ^ C)
# print("Symmetric difference 2:", A ^ C)

# C.add(4)
# C.remove(2)
# print(C)

# Dictionaries 

# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "B.Tech IT"
# }

# print(student["name"])

# student["age"] = 21
# student["city"] = "Chennai"

# print(student.get("email", "Not available"))

# for key, value in student.items():
#     print(key, ":", value)  # City Comes From here 

# del student["city"]

# print(student)

# Najayas 🥀

# numbers = [2, 5, 2, 8, 2, 5]
# targets = [2, 5, 8]

# for target in targets:
#     count = 0
#     for value in numbers:
#         if value == target:
#             count += 1
#     print(target, count)

# Bin baap Ka 🥀

def remove_duplicates_sorted(arr):
    if not arr:
        return []
    write = 1
    for read in range(1, len(arr)):
        if arr[read] != arr[write - 1]:
            arr[write] = arr[read]
            write += 1
    return arr[:write]

def find_maximum(arr):
    maximum = arr[0]
    for value in arr[1:]:
        if value > maximum:
            maximum = value
    return maximum

def count_value(arr, target):
    count = 0
    for value in arr:
        if value == target:
            count += 1
    return count

marks = [35, 40, 40, 55, 60, 60, 72, 85, 90]

print("Unique:", remove_duplicates_sorted(marks.copy()))
print("Maximum:", find_maximum(marks))
print("60 count:", count_value(marks, 60))
print("3rd smallest:", sorted(marks)[2])


