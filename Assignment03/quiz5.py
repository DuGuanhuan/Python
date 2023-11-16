#get input number
num_line = int(input("Enter number of lines: "))
num_perline = int(input("Enter number of numbers on each line: "))

initial_num = 0
#for-loop outputs num_line lines
for i in range(1, num_line + 1):
    
#every line have num_perline number
    for j in range(0, num_perline):
        if(j == num_perline - 1):
            print(f"{initial_num}.")
        else:
            print(initial_num, end=",")
        initial_num += 1