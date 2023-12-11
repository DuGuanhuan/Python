def list_character(word, index_list):
    result = [word[i] for i in index_list if i < len(word)]
    return result

# Example usage:
word = "ABCXYZ"
index_list = [0, 0, 6, 100, 1, 5]
result_list = list_character(word, index_list)
print(result_list)
