# 7. Write a Python program to find the repeated items of a tuple.

def repeated_items(tuple):
    return [item for item in tuple if tuple.count(item) > 1]

tuple = (1, 2, 3, 2, 4, 5, 6, 3, 7, 8, 3, 9)

result = repeated_items(tuple)

print("Original Tuple:", tuple)
print("Repeated Items:", result)
