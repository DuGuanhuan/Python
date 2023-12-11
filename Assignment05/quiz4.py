def odd_indices_characters(sentence):
    char_list = list(sentence)
    result_list = char_list[1::2]
    return result_list

# Get user input for the sentence
user_input = input("Enter a sentence: ")

# Construct the list and print the result
result_list = odd_indices_characters(user_input)
print("List of characters at odd index:")
print(result_list)
