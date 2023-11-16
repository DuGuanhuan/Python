i = int(input("Enter an integer: "))
j = int(input("Enter another integer: "))
if i < j:
    for k in range(i, j+1):
        print(f"{k:5} + {k:5} = {k + k:5}")
elif i > j:
    for k in range(j, i+1):
        print(f"{k:5} + {k:5} = {k + k:5}")
else:
    print(f"{i:5} + {i:5} = {i + i:5}")
