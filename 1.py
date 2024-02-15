# 1.Write a Python program to multiples all the items in a list.

def multiplication(my_list):
    result = 1
    for item in my_list:
        result *= item
    return result

input_value = [1, 2, 3, 4]
my_list = [int(x) for x in input_value]

if my_list:
    result = multiplication(my_list)
    print(result)
else:
    print("Invalid list")



