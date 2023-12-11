word_list = []
count = 1
while True:
    word = input("Enter a word (or enter QUIT to quit): ")
    if word == "QUIT":
        if(count <= 5):
            print("List of last 5 words: ")
            print(word_list)
            break
        else:
            print("List of last 5 words: ")
            print(word_list[-5:])
            break
    else:
        word_list.append(word)
        count += 1