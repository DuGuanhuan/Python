num_item = int(input("How many square numbers to generate? "))
print("Here is a list of generated squares: [",end='')
if num_item == 0:
    print("]")
else:
    i = 0
    while(i < num_item):
        if(i == num_item - 1):
            print(i * i, end=']')
        else:
            print(i * i,end=', ')
        i += 1

# print(']')