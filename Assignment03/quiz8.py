base = input("Enter a word for base: ")
side = input("Enter a word for side: ")
print("Here is the pattern:")
print(f"*{base}*")
for i in range(0, len(side)):
    print(f"{side[i]}{' ' * len(base)}{side[i]}")
print(f"*{base}*")
