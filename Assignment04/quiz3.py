def displayPattern(word, shape):
    lower_word = word.lower()

    if shape == "triangle":
        print("Triangle pattern:")
        for i in range(len(word)):
            print(lower_word[:i + 1].rjust(len(word)))

    elif shape == "rectangle":
        print("Rectangle pattern:")
        for _ in range(len(word)):
            print(lower_word)

    elif shape == "trapezoidal":
        print("Trapezoidal pattern:")
        length = len(word)
        for i in range(0, length):
            spaces = ' ' * (length - i - 1)
            pattern = lower_word[:i + 1] + lower_word[i::-1]
            print(spaces + pattern)

    else:
        print("Unknown shape.")

# Examples usage:
displayPattern(word="One", shape="triangle")
displayPattern(word="gooDDAY", shape="rectangle")
displayPattern(word="OK", shape="trapezoidal")
displayPattern(word="thanks", shape="Hooray")
displayPattern(word="allGood", shape=".~!")
