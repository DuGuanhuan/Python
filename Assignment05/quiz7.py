def add_list(list1, list2):
    # Find the maximum length among the two lists
    result = []

    if len(list1) > len(list2):
        min_length = len(list2)

        for i in range(0, min_length):
            result = result + ([list1[i] + list2[i]])
        result = result + list1[min_length:]
    else:
        min_length = len(list1)
        for i in range(0, min_length):
            result = result + ([list1[i] + list2[i]])
        result = result + list2[min_length:]
    return result


# Example usage:
list1 = [10, 20, 30, 40]
list2 = [7, 9, 21]
result_list = add_list(list1, list2)
print(result_list)
