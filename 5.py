# 5.Use list comprehension to construct a new list but add 6 to each item.
	# list = [24,34,54,45]

original_list = [24, 34, 54, 45]

new_list = [num + 6 for num in original_list]

print("Original List:", original_list)
print("New List (with 6 added to each item):", new_list)
