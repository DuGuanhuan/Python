word_list = []

while True:
    word = input("Enter a word (or type Q to quit): ")
    if word == 'Q':
        print("List of characters: ")
        print(word_list)
        break
    else:
        if len(word) >= 5:
            word_list.append(word[4])
        else:
            continue