word_list = []

while True:
    word = input("Enter a word (or type EXIT to quit): ")
    if word == 'EXIT':
        print(f"Word list you have entered: {word_list}")
        break
    else:
        word_list.append(word)
