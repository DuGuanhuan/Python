def construct_number_list(min_int, max_int):
    result_list = []
    for i in range(max_int, min_int - 1, -1):
        result_list.append(i)
        result_list.append(i)
        result_list.append(i)
    return result_list

# Get user input for min and max integers
min_integer = int(input("Enter a min integer: "))
max_integer = int(input("Enter a max integer: "))

# Construct the list and print the result
result_list = construct_number_list(min_integer, max_integer)
print("Here is a list of numbers constructed:")
print(result_list)
