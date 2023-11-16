# #get input
option = input("Enter option A or B: ")
if (option == 'A'):
    word = input("Enter a word: ")
    for i in range(0, len(word)):
        print(f"Index {i} -> letter {word[i]}")

elif (option == 'B'):
    integer = int(input("Enter a positive integer: "))
    for j in range(1, integer + 1):
        print(f"{integer} - {j} = {integer - j}")
    print("Result is zero, stop now!")
else:
    print("We only support A or B")
    print("Good bye!")
    

