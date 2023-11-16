input_string = input("Enter some characters: ")
num_characters = int(input("Enter the number of characters to be displayed: "))

if num_characters <= len(input_string):
    print('-'.join(input_string[:num_characters]))
else:
    print('-'.join(input_string))
