def jersey_num_iron_on():
    while True:
        content = input("Please enter a name with an odd number of (at most 9) letters: ")
        if len(content) % 2 == 1 and len(content) <= 9:
            break
    while True:
        num = int(input("Please enter an integer (0 - 999): "))
        if num in range(0,1000):
            break
    if (num <= 99 and num >= 10):
        num = str(num)
        num = num[0] + ' ' + num[1]
    else:
        num = str(num)

    upper_content = content.upper()
    print("  ___       ___")
    print(" /   \_____/   \\")
    print("|_             _|")
    print(f"  |{upper_content.center(11)}|")
    print("  |           |")
    print(f"  |{num.center(11)}|")
    print("  |           |")
    print("  +___________+")



