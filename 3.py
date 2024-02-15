# 3.Write a Python program to count the number of strings where the string length is 2 or more.
	# Sample List : ['abc', 'xyz', 'aba', '1']
	# Expected Result : 3

def strings_length(my_list):
    count = 0
    for string in my_list:
        if len(string) >= 2:
            count += 1
    return count

input_value = input("Enter list:")
user_list = input_value.split()

result = strings_length(user_list)

print("User List:", user_list)
print("Number of strings:", result)


