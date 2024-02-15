# 4.Write a Python program to print the numbers of a specified list after removing even numbers from it
	# list = [24,34,53,65,78,93,23,42]

def remove_even(list):
    return [num for num in list if num % 2 != 0]

list = [24, 34, 53, 65, 78, 93, 23, 42]

result = remove_even(list)

print("Original List:", list)
print("List after removing even numbers:", result)

