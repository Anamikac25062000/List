# 2.Write a Python program to remove duplicates from a list

def remove_duplicates(list1):
    return list(set(list1))

input_value = [1, 2, 3, 4, 4, 2, 5]
original_list = input_value

result = remove_duplicates(original_list)

print("Original List:", original_list)
print("List with Duplicates Removed:", result)
